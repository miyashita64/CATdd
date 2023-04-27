import re
from file_interface import FileInterface

class ResultAnalyzer:
    """テスト結果解析クラス"""
    @staticmethod
    def analyze(log_path):
        """テスト結果から失敗したテストケースについての情報を抽出する.

        Args:
            log_path: String
        Return:
            失敗したテストケースデータのリスト: [{path: String, testcase_names: [String]}]
        """
        failed_start_pattern = r"\d+: (.+):(\d+): Failure"
        errors = []
        in_error = False
        log = FileInterface.read(log_path)
        for i, line in enumerate(log.split("\n")):
            start_match = re.match(failed_start_pattern, line)
            if in_error:
                errors[-1]["message"] += "\n" + line
                if "FAILED" in line:
                    # テストケース名の抽出
                    errors[-1]["testcase_name"] = line.split("\x1b[m")[1].split(" ")[0].split(".")[1]
                    in_error = False
            elif start_match:
                in_error = True
                error = {
                    "path":  start_match.group(1),
                    "line":  int(start_match.group(2)),
                    "message": line,
                    "testcase_name": "",
                }
                errors.append(error)
        # 整形
        failed_test_datas = []
        failed_test_paths = list(set(map(lambda e: e["path"], errors)))
        for test_path in failed_test_paths:
            test_data = {
                "path": test_path,
                "testcase_names": list(set(map(lambda e: e["testcase_name"], errors))),
            }
            failed_test_datas.append(test_data)
        return failed_test_datas