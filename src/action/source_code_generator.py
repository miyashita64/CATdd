import re
from enum import Enum
from common.catdd_info import CATddInfo
from common.log import Log
from common.file_interface import FileInterface
from llm.gpt_interface import GPTInterface
from llm.prompt import Prompt, PromptElement
from object.source_code import SourceCode

class Priority(Enum):
    GEN = 5
    BASE = 3
    ANOTOHER = 2
    FIRST_RESULT = 4
    RESULT = 1

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
            # Log.log(test_result.stderr)
            source_codes = self.generate_testable_code(test_result)
        return source_codes

    def generate_passable_code(self, test_result):
        """テストにパスできるソースコードを生成する"""
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
            failed_testcase_prompt_elms = [PromptElement(
                    f"{testcase_result.code}\n{testcase_result.stdout}\n",
                    Priority.FIRST_RESULT.value if testcase_result is testcase_results[0] else Priority.RESULT.value
                ) for testcase_result in testcase_results]
            # ヘッダーファイルとソースファイルについて
            file_types = ["header", "source"]
            for file_type in file_types:
                # 今対象としているコード[header/source]について
                file_type_extension = "h" if file_type == "header" else "cpp"
                file_type_path = existed_header_file_path if file_type == "header" else existed_source_file_path
                file_type_code = existed_header_code if file_type == "header" else existed_source_code
                # 今対象としていないコード[source/header]について
                another_type = "source" if file_type == "header" else "header"
                another_type_code =  existed_source_code if file_type == "header" else existed_header_code

                # プロンプトのパーツ作成
                # 既存のソースコード[header/source]
                how_generate_prompt_value = "generating new code"
                base_code_prompt_value = ""
                if file_type_code != "":
                    # 既存のソースコードが存在する場合
                    how_generate_prompt_value = "rewriting the base code"
                    base_code_prompt_value = f"\n### {file_type} file (base code):\n{existed_source_code}\n"
                base_code_prompt_elm = PromptElement(base_code_prompt_value, Priority.BASE.value)
                # 既存のソースコードと関連するソースコード[source/header]
                another_code_prompt_value = ""
                if another_type_code != "":
                    another_code_prompt_value = f"\n### {another_type} file:\n{another_type_code}\n"
                another_code_prompt_elm = PromptElement(another_code_prompt_value, Priority.ANOTOHER.value)

                # プロンプト作成
                generate_code_prompt_value = f"Implement a {file_type} file by {how_generate_prompt_value} that will pass the following test cases.\n" \
                                           + f"However, only the {file_type} file out of the two files, source file and header file.\n" \
                                           + f"\n### Failed test cases to pass:\n"
                generate_code_prompt_elm = PromptElement(generate_code_prompt_value, Priority.GEN.value)

                generate_code_prompt = Prompt([generate_code_prompt_elm,
                                               *failed_testcase_prompt_elms,
                                               base_code_prompt_elm,
                                               another_code_prompt_elm],
                                              4096 * 0.5    # 4096 = GPT-3.5-turboの最大の入出力トークン数
                                             )
                assistant_prompt_value = f"### correction {file_type} file:\n"
                # プロンプトを送信しソースコード生成
                response = GPTInterface.request_code(generate_code_prompt.value, assistant_prompt_value)
                source_code_path = file_type_path if file_type_path is not None else CATddInfo.path(f"output/{class_name}.{file_type_extension}")
                source_codes += [SourceCode(source_code_path, response)]
                # ヘッダファイルを生成した際に、ソースコードに反映するために、ヘッダファイルのコードを更新する
                if file_type == "header":
                    existed_header_code = response
        return source_codes

    def generate_testable_code(self, test_result):
        """テスト実行可能なソースコードを生成する"""
        source_codes = []

        # テスト結果(コンパイルエラー)が膨大過ぎる場合を考慮
        test_result_value = test_result.stderr
        max_test_result_length = 2000
        if len(test_result.stderr) > max_test_result_length:
            # エラー文を短縮する
            test_result_value = test_result.stderr[:max_test_result_length]

        # 修正すべきファイルを決定する
        user_prompt = "Extract the path to the file to be corrected from the error text.\n" + test_result_value + "\nfile path: "
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
            another_type_code =  bug_source_code if file_type == "header" else bug_header_code

            # プロンプトのパーツ作成
            # 既存のソースコード[header/source]
            how_generate_prompt_value = "generating new code"
            base_code_prompt_value = ""
            if file_type_code != "":
                # 既存のソースコードが存在する場合
                how_generate_prompt_value = "rewriting the base code"
                base_code_prompt_value = f"\n### {file_type} file (base code):\n{bug_source_code}\n"
            base_code_prompt_elm = PromptElement(base_code_prompt_value, Priority.BASE.value)
            # 既存のソースコードと関連するソースコード[source/header]
            another_code_prompt_value = ""
            if another_type_code != "":
                another_code_prompt_value = f"\n### {another_type} file:\n{another_type_code}\n"
            another_code_prompt_elm = PromptElement(another_code_prompt_value, Priority.ANOTOHER.value)
            # テストコード
            test_code_prompt_value = ""
            if test_file_path != "":
                test_code = FileInterface.read(test_file_path)
                test_code_prompt_value = f"\n### However, the code should pass the following tests:\n{test_code}\n"
            test_code_prompt_elm = PromptElement(test_code_prompt_value, Priority.RESULT.value)

            # プロンプト作成
            generate_code_prompt_value = f"Implement a {file_type} file by {how_generate_prompt_value} resolve the following errors.\n" \
                                       + f"Only the {file_type} file out of the two files, source file and header file.\n" \
                                       + f"\n### Error:\n{test_result_value}"
            generate_code_prompt_elm = PromptElement(generate_code_prompt_value, Priority.GEN.value)
            generate_code_prompt = Prompt([generate_code_prompt_elm,
                                           test_code_prompt_elm,
                                           base_code_prompt_elm,
                                           another_code_prompt_elm],
                                          4096 * 0.5)
            assistant_prompt_value = f"### generated {file_type} file:"

            # プロンプトを送信しソースコード生成
            response = GPTInterface.request_code(generate_code_prompt.value, assistant_prompt_value)
            source_code_path = file_type_path if file_type_path is not None else CATddInfo.path(f"output/{class_name}.{file_type_extension}")
            source_codes += [SourceCode(source_code_path, response)]
            # ヘッダファイルを生成した際に、ソースコードに反映するために、ヘッダファイルのコードを更新する
            if file_type == "header":
                bug_header_code = response
        return source_codes
