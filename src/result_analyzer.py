import re
from file_interface import FileInterface

class ResultAnalyzer:
    """テスト結果解析クラス"""
    @staticmethod
    def analyze(log_path):
        """テスト結果のログファイルを解決し、失敗したテストケースデータを抽出する.
        
        Args:
            log_path: String
        Return:
            失敗したテストケースデータのリスト: [{path: String, testcases_names: [String], labels: [String]}]
        """
        log = FileInterface.read(log_path)
        errors = ResultAnalyzer.test_result_analyze(log)
        errors += ResultAnalyzer.compile_error_analyze(log)

        # 整形
        failed_test_datas = []
        failed_test_class_names = list(set(map(lambda e: e["class_name"], errors)))
        for class_name in failed_test_class_names:
            test_data = {
                "class_name": class_name,
                "path": list(set(map(lambda e: e["path"], errors)))[0],
                "testcase_names": list(set(map(lambda e: e["testcase_name"], errors))),
                "labels": list(set(map(lambda e: e["label"], errors))),
            }
            failed_test_datas.append(test_data)
        return failed_test_datas

    def compile_error_analyze(log):
        """テスト結果から特定のエラーが発生したテストケースデータを抽出する.
        
        Args:
            log: String
        Return:
            失敗したテストケース結果のリスト: [{path: String, line: Int, message: String, testcase_names: String, label: String}]
        """
        no_such_file_pattern = r"^(.*\/.+):(\d+):\d+: fatal error: (.+): No such file or directory"
        has_no_member_pattern = r"^(.*\/.+):(\d+):\d+: error: ‘(.+)’ has no member named ‘(.+)’"
        undefined_pattern = r"^(.*\/.+):(\d+):\s*undefined reference to"
        testcase_name_pattern = r"/.*?: in function `.*?::.*?_(.*?)_Test::TestBody\(\)':"
        errors = []
        pre_line = ""
        for i, line in enumerate(log.split("\n")):
            no_such_file_match = re.match(no_such_file_pattern, line)
            has_no_member_match = re.match(has_no_member_pattern, line)
            undefined_match = re.match(undefined_pattern, line)
            testcase_name_match = re.search(testcase_name_pattern, pre_line)
            if no_such_file_match:
                error = {
                    "class_name": no_such_file_match.group(3).split(".")[0],
                    "path": no_such_file_match.group(1),
                    "line": int(no_such_file_match.group(2)),
                    "message": line,
                    "testcase_name": "TEST",
                    "label": f"NO_SUCH_FILE {no_such_file_match.group(3)}",
                }
                errors.append(error)
            elif has_no_member_match:
                path = has_no_member_match.group(1)
                error = {
                    "class_name": path.split("/")[-1].split("Test.")[0].split(".")[0],
                    "path": path,
                    "line": int(has_no_member_match.group(2)),
                    "message": line,
                    "testcase_name": "TEST",
                    "label": f"HAS_NO_MEMBER {has_no_member_match.group(3)} {has_no_member_match.group(4)}",
                }
                errors.append(error)
            elif undefined_match and testcase_name_match:
                path = has_no_member_match.group(1)
                error = {
                    "class_name": path.split("/")[-1].split("Test.")[0].split(".")[0],
                    "path": path,
                    "line": int(undefined_match.group(2)),
                    "message": ("\n").join([pre_line, line]),
                    "testcase_name": testcase_name_match.group(1),
                    "label": testcase_name_match.group(1),
                }
                errors.append(error)
            pre_line = line
        return errors

    def test_result_analyze(log):
        """テスト結果から失敗したテストケースについての情報を抽出する.

        Args:
            log: String
        Return:
            失敗したテストケース結果のリスト: [{path: String, line: Int, message: String, testcase_names: String, label: String}]
        """
        failed_start_pattern = r"\d+: (.+):(\d+): Failure"
        errors = []
        in_error = False
        for i, line in enumerate(log.split("\n")):
            start_match = re.match(failed_start_pattern, line)
            if in_error:
                errors[-1]["message"] += "\n" + line
                if "FAILED" in line:
                    # テストケース名の抽出
                    errors[-1]["testcase_name"] = line.split("\x1b[m")[1].split(" ")[0].split(".")[1]
                    errors[-1]["label"] = errors[-1]["testcase_name"]
                    in_error = False
            elif start_match:
                in_error = True
                path = has_no_member_match.group(1)
                error = {
                    "class_name": path.split("/")[-1].split("Test.")[0].split(".")[0],
                    "path": path,
                    "line":  int(start_match.group(2)),
                    "message": line,
                    "testcase_name": "",
                    "label": "",
                }
                errors.append(error)
        return errors