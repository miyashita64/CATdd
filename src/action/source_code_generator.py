from common.catdd_info import CATddInfo
from llm.gpt_interface import GPTInterface
from object.source_code import SourceCode

class SourceCodeGenerator:
    def generate(self, test_result):
        if test_result.is_passed:
            # すべてのテストにパスしていた場合
            Log.info("Test is already passed.")
            return []
        elif test_result.is_exec_test:
            # いくつかのテストケースが失敗していた場合
            test_targets = {}
            # テスト結果をテスト対象毎にグルーピング
            for testcase_result in test_result.testcase_results:
                if not testcase_result.is_passed:
                    test_target = testcase_result.class_name
                    if test_target not in test_targets:
                        test_targets[test_target] = []
                    test_targets[test_target] += [testcase_result]
            # テスト対象毎にソースコード生成
            source_codes = []
            for test_target in test_targets:
                # TODO:既存のソースコードを探索する
                testcase_results = test_targets[test_target]
                failed_testcase_prompt = [testcase_result.code + "\n" + testcase_result.stdout for testcase_result in testcase_results]
                user_prompt = "以下のエラーを解消するようなソースコードを書いて。\n" + "\n".join(failed_testcase_prompt)
                response = GPTInterface.request("gpt-3.5-turbo", user_prompt)
                # response = GPTInterface.request("text-davinci-003", user_prompt)
                source_code_path = CATddInfo.path(f"output/{test_target}.cpp")
                source_codes += [SourceCode(source_code_path, response)]
            return source_codes
        else:
            # テストが実行できなかった場合(コンパイルエラーなど)
            Log.log(test_result.stderr)
            return []