"""テストを実行するクラス"""

import subprocess
from common.catdd_info import CATddInfo
from common.log import Log
from object.test_result import TestResult

class Tester:
    """テストを実行するクラス"""
    def test(self, timelimit=300):
        """テスト実行"""
        try:
            command = f"cd {CATddInfo.test_exec_path} && {CATddInfo.test_exec_cmd}"
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timelimit)
            return TestResult(result.stdout, result.stderr)
        except subprocess.TimeoutExpired as e:
            Log.warning("Timed out during testing.")
            return TestResult(e.output, "Timed out during testing.")
