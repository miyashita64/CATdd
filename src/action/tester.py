"""テストを実行するクラス"""

import subprocess
from common.catdd_info import CATddInfo
from object.test_result import TestResult

class Tester:
    """テストを実行するクラス"""
    def test(self):
        """テスト実行"""
        command = f"cd {CATddInfo.test_exec_path} && {CATddInfo.test_exec_cmd}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return TestResult(result.stdout, result.stderr)
