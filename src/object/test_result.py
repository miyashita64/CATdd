import re
from common.catdd_info import CATddInfo
from common.log import Log
from object.test_code import TestCode

class TestResult:
    """テスト結果を保持するクラス."""
    def __init__(self, result_stdout, result_stderr):
        """コンストラクタ."""
        self.stdout = result_stdout
        self.stderr = result_stderr
        self.testcase_results = self.generate_testcase_results()
        self.is_exec_test = len(self.testcase_results) > 0
        self.is_passed = self.is_exec_test and len([result for result in self.testcase_results if not result.is_passed]) == 0

    def print(self):
        """テスト結果を簡単に表示する."""
        if self.is_passed:
            # テスト全通過
            Log.success("\nPasses all tests!!\n")
        else:
            # テストをパスできなかった場合
            if self.is_exec_test:
                # テストは実行できた場合
                # 失敗したテストケースを抽出
                failed_testcase_results = [testcase_result for testcase_result in self.testcase_results if not testcase_result.is_passed]
                Log.warning(f"Failed {len(failed_testcase_results)} test.")
                # 失敗してたテストケースごとのテスト結果を表示
                for failed_testcase_result in failed_testcase_results:
                    Log.log(failed_testcase_result.stdout)
            else:
                # テストを実行できなかった場合
                Log.warning("Could not run test.")
                Log.log(self.stderr)

    def generate_testcase_results(self):
        """標準出力からテストケース毎の結果を判定する."""
        testcase_results = []
        # 標準出力におけるテストケースの実行状況に対する正規表現のパターン定義
        testcase_run_pattern = r"^.+\[\s+RUN\s+] .+\[m(?P<testcase_name>\S+?)$"                     # 開始
        testcase_ok_pattern = r"^.+\[\s+OK\s+] .+\[m(?P<testcase_name>\S+?) \(\d+ ms\)$"            # 通過
        testcase_failed_pattern = r"^.+\[\s+FAILED\s+] .+\[m(?P<testcase_name>\S+?) \(\d+ ms\)$"    # 失敗
        # 各実行状況が変化した行を検出
        testcase_run_matches = list(re.finditer(testcase_run_pattern, self.stdout, re.MULTILINE))
        testcase_ok_matches = list(re.finditer(testcase_ok_pattern, self.stdout, re.MULTILINE))
        testcase_failed_matches = list(re.finditer(testcase_failed_pattern, self.stdout, re.MULTILINE))

        if CATddInfo.is_fast_mode and len(testcase_run_matches) != len(testcase_ok_matches):
            # テスト結果の判定を高速化
            return [TestcaseResult("blankTest.fastFailedTest", False ,"")]

        # テストケース毎の出力の範囲を特定し保持
        for start_match in testcase_run_matches:
            end_span = None
            is_testcase_passed = False
            # 同じテストケース名に関する変化を含む行を抽出し位置を保持
            testcase_name = start_match.group("testcase_name")
            ok_spans = [ok_match.span() for ok_match in testcase_ok_matches if ok_match.group("testcase_name") == testcase_name]
            if len(ok_spans) > 0:
                # テストをパスした場合
                end_span = ok_spans[0]
                is_testcase_passed = True
            else:
                # 同じテストケース名に関する変化を含む行を抽出し位置を保持
                failed_spans = [failed_match.span() for failed_match in testcase_failed_matches if failed_match.group("testcase_name") == testcase_name]
                if len(failed_spans) > 0:
                    # テストに失敗した場合
                    end_span = failed_spans[0]
            if end_span is not None:
                # テストケースの範囲を特定できた場合
                testcase_stdout = self.stdout[start_match.span()[0]:end_span[1]]
                testcase_results += [TestcaseResult(testcase_name, is_testcase_passed, testcase_stdout)]
            else:
                # テストケースの終了を検出できなかった場合(セグフォなどでテストが異常終了)
                Log.warning(f"Could not confirm completion of the '{testcase_name}'.\nTesting may have been interrupted due to segmentation fault or other reasons.")
                start = start_match.span()[0]
                # とりあえず、テスト開始から350文字を出力とする
                testcase_stdout = self.stdout[start:start+350]
                testcase_results += [TestcaseResult(testcase_name, is_testcase_passed, testcase_stdout)]
        return testcase_results

class TestcaseResult:
    """テストケース毎のテスト結果を保持する."""

    def __init__(self, name, is_testcase_passed, stdout):
        """コンストラクタ."""
        self.name = name
        self.class_name = name.split(".")[0]
        if self.class_name.endswith('Test'):                                        
            self.class_name = self.class_name[:-4]                                             
        self.is_passed = is_testcase_passed
        self.stdout = stdout
        failed_test_file_path_pattern = r"\d+:\s+(?P<test_file_path>\S+?):(?P<assert_row>\d+):\sFailure"
        match = re.search(failed_test_file_path_pattern, self.stdout)
        if match is not None and not CATddInfo.is_fast_mode:
            # テストケースが失敗していた場合
            self.file_path = match.group("test_file_path")
            self.assert_row = int(match.group("assert_row"))
            test_code = TestCode(self.file_path)
            self.code = test_code.slice_testcase(self.assert_row)
        else:
            # テストケース失敗が確認できなかった場合
            self.file_path = ""
            self.assert_row = -1
            self.code = ""
