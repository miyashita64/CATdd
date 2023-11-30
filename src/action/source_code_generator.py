from llm.gpt_interface import GPTInterface
from object.source_code import SourceCode

class SourceCodeGenerator:
    def generate(self, test_result):
        # テスト結果をテスト対象毎にグルーピング
        test_targets = {}
        for testcase_result in test_result.testcase_results:
            if not testcase_result.is_passed:
                test_target = testcase_result.name.split(".")[0]
                if test_target not in test_targets:
                    test_targets[test_target] = []
                test_targets[test_target] += [testcase_result]
        # テスト対象毎にソースコード生成
        source_codes = []
        for test_target in test_targets:
            testcase_results = test_targets[test_target]
            failed_testcase_prompt = [testcase_result.code + "\n" + testcase_result.stdout for testcase_result in testcase_results]
            response = GPTInterface.request("以下のエラーを解決して。\n" + "\n".join(failed_testcase_prompt))
            print("~~~~~~~~~~~~~~~~~~~~")
            print("\n".join(failed_testcase_prompt))
            print("====================")
            print(response)
            print("#####################")
            source_codes += [SourceCode("", response)]
        return source_codes