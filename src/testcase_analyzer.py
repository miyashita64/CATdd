from file_interface import FileInterface

class TestcaseAnalyzer:
    @staticmethod
    def analyze(test_data):
        """テストデータを受け取り、失敗したテストケースの内容を抽出する関数.

        Arg:
            test_data: {path: String, testcase_names: [String]}
        Return:
            失敗したテストケースだけを結合した文字列: String
        """
        failed_testcases = []
        failed_testcase = ""
        testcode = FileInterface.read(test_data["path"])
        in_testcase = False
        in_block = False
        bracket_count = 0
        for line in testcode.split("\n"):
            if "TEST" in line and any(testcase_name in line for testcase_name in test_data["testcase_names"]):
                failed_testcase = ""
                in_testcase = True
                if "{" not in line:
                    in_block = False
            if in_testcase:
                failed_testcase += line + "\n"
                if "{" in line:
                    bracket_count += 1
                    in_block = True
                if "}" in line:
                    bracket_count -= 1
                if bracket_count == 0 and in_block:
                    in_testcase = False
                    in_block = False
                    failed_testcases.append(failed_testcase)
        return failed_testcases