"""テストを実行するクラス"""

import subprocess
from object.test_result import TestResult

class Tester:
    """テストを実行するクラス"""
    def __init__(self, test_exec_path, test_exec_cmd):
        """コンストラクタ"""
        self.test_exec_path = test_exec_path
        self.test_exec_cmd = test_exec_cmd

    def test(self):
        """テスト実行"""
        command = f"cd {self.test_exec_path} && {self.test_exec_cmd}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return TestResult(result.stdout, result.stderr)
