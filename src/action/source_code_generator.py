import re
from common.catdd_info import CATddInfo
from common.log import Log
from common.file_interface import FileInterface
from llm.gpt_interface import GPTInterface
from object.source_code import SourceCode

class SourceCodeGenerator:
    def generate(self, test_result):
        source_codes = []
        if test_result.is_passed:
            # すべてのテストにパスしていた場合
            Log.info("Test is already passed.")
        elif test_result.is_exec_test:
            # いくつかのテストケースが失敗していた場合
            Log.info("Edit source code to pass the test cases.")
            source_codes = self.generate_passable_code(test_result)
        else:
            # テストが実行できなかった場合(コンパイルエラーなど)
            Log.info("Fix compile errors.")
            Log.log(test_result.stderr)
            source_codes = self.generate_testable_code(test_result)
        return source_codes

    def generate_passable_code(self, test_result):
        source_codes = []
        # テスト結果をテスト対象のクラス名ごとにグルーピング
        failed_testcase_results = [testcase_result for testcase_result in test_result.testcase_results if not testcase_result.is_passed]
        failed_testcase_results_by_class = {}
        for testcase_result in failed_testcase_results:
            class_name = testcase_result.class_name
            failed_testcase_results_by_class.setdefault(class_name, []).append(testcase_result)
        # テスト対象毎にソースコード生成
        for class_name in failed_testcase_results_by_class:
            # 既存のソースコードを探索する
            existed_header_file_path = FileInterface.search(f"{class_name}.h", CATddInfo.src_path)
            existed_header_code = "" if existed_header_file_path is None else FileInterface.read(existed_header_file_path)
            existed_source_file_path = FileInterface.search(f"{class_name}.cpp", CATddInfo.src_path)
            existed_source_code = "" if existed_source_file_path is None else FileInterface.read(existed_source_file_path)
            # 各テストケースの結果をまとめる
            testcase_results = failed_testcase_results_by_class[class_name]
            failed_testcase_prompt = "\n".join([testcase_result.code + "\n" + testcase_result.stdout for testcase_result in testcase_results])
            # ヘッダーファイルとソースファイルについて
            file_types = ["header", "source"]
            for file_type in file_types:
                # 今対象としているコード[header/source]について
                file_type_extension = "h" if file_type == "header" else "cpp"
                file_type_path = existed_header_file_path if file_type == "header" else existed_source_file_path
                file_type_code = existed_header_code if file_type == "header" else existed_source_code
                # 今対象としていないコード[source/header]について
                another_type = "source" if file_type == "header" else "header"
                another_type_code =  existed_source_code if another_type == "header" else existed_header_code
                # プロンプトのパーツ作成
                how_generate_prompt = "generating new code"
                base_code_prompt = ""
                if file_type_code != "":
                    # 既存のソースコードが存在する場合
                    how_generate_prompt = "rewriting the base code"
                    base_code_prompt = f"\n### {file_type} file (base code):\n{existed_source_code}\n"
                another_code_prompt = ""
                if another_type_code != "":
                    another_code_prompt = f"\n### {another_type} file: {another_type_code}\n"
                # プロンプト作成
                generate_code_prompt = f"Implement a {file_type} file by {how_generate_prompt} that will pass the following test cases.\n" \
                                     + f"However, only the {file_type} file out of the two files, source file and header file.\n" \
                                     + f"\n### Failed test cases to pass:\n{failed_testcase_prompt}\n" \
                                     + base_code_prompt \
                                     + another_code_prompt
                # プロンプトを送信しソースコード生成
                response = GPTInterface.request_code(generate_code_prompt)
                source_code_path = file_type_path if file_type_path is not None else CATddInfo.path(f"output/{class_name}.{file_type_extension}")
                source_codes += [SourceCode(source_code_path, response)]
                # ヘッダファイルを生成した際に、ソースコードに反映するために、ヘッダファイルのコードを更新する
                if file_type == "header":
                    existed_header_code = response
        return source_codes

    def generate_testable_code(self, test_result):
        source_codes = []
        # 修正すべきファイルを決定する
        user_prompt = "Extract the path to the file to be corrected from the error text.\n" + test_result.stderr + "\nfile path: "
        bug_source_file_path = GPTInterface.request(user_prompt)
        bug_file_name = bug_source_file_path.split("/")[-1]
        test_file_path = ""
        if "test" in bug_file_name.lower():
            # テストに問題があると判定された場合
            # TDD(CATdd)はテストに問題はないことを前提とするため、テスト対象の問題として扱う
            test_file_path = bug_source_file_path
            bug_file_name = re.sub(r"(?i)test", "", bug_file_name)
            bug_source_file_path = FileInterface.search(bug_file_name, CATddInfo.src_path)
        class_name = bug_file_name.split(".")[0]
        if bug_source_file_path is None:
            bug_source_file_path = CATddInfo.output_path(bug_file_name)
        bug_header_file_path = f"{bug_source_file_path[:-4]}.h"
        # バグがあると思われるファイルの中身を参照する
        bug_header_code = FileInterface.read(bug_header_file_path)
        bug_source_code = FileInterface.read(bug_source_file_path)
        # ヘッダーファイルとソースファイルについて
        file_types = ["header", "source"]
        for file_type in file_types:
            # 今対象としているコード[header/source]について
            file_type_extension = "h" if file_type == "header" else "cpp"
            file_type_path = bug_header_file_path if file_type == "header" else bug_source_file_path
            file_type_code = bug_header_code if file_type == "header" else bug_source_code
            # 今対象としていないコード[source/header]について
            another_type = "source" if file_type == "header" else "header"
            another_type_code =  bug_source_code if another_type == "header" else bug_header_code
            # プロンプトのパーツ作成
            how_generate_prompt = "generating new code"
            base_code_prompt = ""
            if file_type_code != "":
                # 既存のソースコードが存在する場合
                how_generate_prompt = "rewriting the base code"
                base_code_prompt = f"\n### {file_type} file (base code):\n{bug_source_code}\n"
            another_code_prompt = ""
            if another_type_code != "":
                another_code_prompt = f"\n### {another_type} file: {another_type_code}\n"
            test_code_prompt = ""
            if test_file_path != "":
                test_code = FileInterface.read(test_file_path)
                test_code_prompt = f"\n### However, the code should pass the following tests:\n{test_code}\n"
            # プロンプト作成
            generate_code_prompt = f"Implement a {file_type} file by {how_generate_prompt} resolve the following errors.\n" \
                                    + f"However, only the {file_type} file out of the two files, source file and header file.\n" \
                                    + f"\n### Error:\n{test_result.stderr}" \
                                    + test_code_prompt \
                                    + base_code_prompt \
                                    + another_code_prompt
            # プロンプトを送信しソースコード生成
            response = GPTInterface.request_code(generate_code_prompt)
            source_code_path = file_type_path if file_type_path is not None else CATddInfo.path(f"output/{class_name}.{file_type_extension}")
            source_codes += [SourceCode(source_code_path, response)]
            # ヘッダファイルを生成した際に、ソースコードに反映するために、ヘッダファイルのコードを更新する
            if file_type == "header":
                bug_header_code = response
        return source_codes
