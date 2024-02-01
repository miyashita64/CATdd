import re
from enum import Enum
from common.catdd_info import CATddInfo
from common.log import Log
from common.file_interface import FileInterface
from llm.gpt_interface import GPTInterface
from llm.prompt import GeneratePassableCodePrompt, GenerateTestableCodePrompt
from object.source_code import SourceCode
from object.test_code import TestCode

class SourceCodeGenerator:
    """ソースコードを生成するクラス."""
    def generate(self, test_result):
        """ソースコードを生成する.
        
        Args:
            test_result (TestResult): テスト結果
        """
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
            source_codes = self.generate_testable_code(test_result)
        return source_codes

    def generate_passable_code(self, test_result):
        """テストにパスできるソースコードを生成する."""
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
            existed_header_code = FileInterface.read(existed_header_file_path)
            existed_source_file_path = FileInterface.search(f"{class_name}.cpp", CATddInfo.src_path)
            existed_source_code = FileInterface.read(existed_source_file_path)
            # 各テストケースの結果をまとめる
            failed_testcase_results = failed_testcase_results_by_class[class_name]
            # ヘッダーファイルとソースファイルについて
            file_types = ["header", "source"]
            for file_type in file_types:
                is_header_type = file_type == "header"
                file_type_extension = "h" if is_header_type else "cpp"
                file_type_path = existed_header_file_path if is_header_type else existed_source_file_path
                # プロンプト生成
                generate_code_prompt = GeneratePassableCodePrompt(class_name, is_header_type, failed_testcase_results, existed_header_code, existed_source_code)
                assistant_prompt_value = f"### correction {file_type} file ({class_name}.{file_type_extension}):\n"
                # プロンプトを送信しソースコード生成
                response = GPTInterface.request_code(generate_code_prompt.value, assistant_prompt_value)
                source_code_path = file_type_path if file_type_path is not None else CATddInfo.path(f"output/{class_name}.{file_type_extension}")
                source_codes += [SourceCode(source_code_path, response)]
                # ヘッダファイルを生成した際に、ソースコードに反映するために、ヘッダファイルのコードを更新する
                if file_type == "header":
                    existed_header_code = response
        return source_codes

    def generate_testable_code(self, test_result):
        """テスト実行可能なソースコードを生成する."""
        source_codes = []

        # テスト結果(コンパイルエラー)が膨大過ぎる場合を考慮
        test_result_value = test_result.stderr
        max_test_result_length = 2000
        if len(test_result.stderr) > max_test_result_length:
            # エラー文を短縮する
            test_result_value = test_result.stderr[:max_test_result_length]

        # 修正すべきファイルを決定する
        user_prompt = "Extract the path to the file to be corrected from the error text.\n" + test_result_value + "\n"
        bug_source_file_path = GPTInterface.request_path(user_prompt)
        bug_file_name = bug_source_file_path.split("/")[-1]
        # 問題が起きているテストコードを特定する
        user_prompt = "Extract the path from the error text to the test code in which the error is occurring.\n" + test_result_value + "\n"
        test_file_path = GPTInterface.request_path(user_prompt)
        test_code = TestCode(test_file_path)
        if "test" in bug_file_name.lower():
            # テストに問題があると判定された場合
            if test_code.code == "":
                test_file_path = bug_source_file_path
                test_code = TestCode(test_file_path)
            # TDD(CATdd)はテストに問題はないことを前提とするため、テスト対象の問題として扱う
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
            is_header_type = file_type == "header"
            file_type_extension = "h" if is_header_type else "cpp"
            file_type_path = bug_header_file_path if is_header_type else bug_source_file_path
            # プロンプト生成
            generate_code_prompt = GenerateTestableCodePrompt(class_name, is_header_type, test_result_value, test_code.code, bug_header_code, bug_source_code)
            assistant_prompt_value = f"### generated {file_type} file({class_name}.{file_type_extension}): "
            # プロンプトを送信しソースコード生成
            response = GPTInterface.request_code(generate_code_prompt.value, assistant_prompt_value)
            source_code_path = file_type_path if file_type_path is not None else CATddInfo.path(f"output/{class_name}.{file_type_extension}")
            source_codes += [SourceCode(source_code_path, response)]
            # ヘッダファイルを生成した際に、ソースコードに反映するために、ヘッダファイルのコードを更新する
            if file_type == "header":
                bug_header_code = response
        return source_codes
