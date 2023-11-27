"""テストを実行するクラス"""

import subprocess
from common.catdd_info import CATddInfo
from common.log import Log
from object.test_result import TestResult

class Tester:
    """テストを実行するクラス"""
    def test(self):
        """テスト実行"""
        Log.log("Testing ... ", end="")
        command = f"cd {CATddInfo.test_exec_path} && {CATddInfo.test_exec_cmd}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        Log.success("Finish!")
        return TestResult(result.stdout, result.stderr)
