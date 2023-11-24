"""テストを実行するクラス"""

import subprocess

class Tester:
    log_dir = "logs/"
    def __init__(self, test_exec_path, test_exec_cmd):
        self.test_exec_path = test_exec_path
        self.test_exec_cmd = test_exec_cmd

    def test(self):
        command = f"cd {self.test_exec_path} && {self.test_exec_cmd}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # print("result.stdout", result.stdout)
        print("result.stderr", result.stderr)

    @classmethod
    def log(cls, log_str):
        pass