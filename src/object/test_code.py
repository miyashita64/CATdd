import re
from common.log import Log
from common.file_interface import FileInterface

class TestCode:
    """テストコードを保持するクラス"""

    def __init__(self, file_path):
        """コンストラクタ"""
        # LLMにパスを聞いた際に「何かしらの説明文:　`パス`」と出力された場合の対処
        self.path = FileInterface.parse_path(file_path)
        self._code = FileInterface.read(self.path)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def lines(self):
        return self._code.split("\n")

    def slice_testcase(self, row):
        """指定された行を含むテストケースのコードを抽出する"""
        before_code, nest = self.slice_up("\n".join(self.lines[:row]))
        after_code, nest = self.slice_down("\n".join(self.lines[row:]), nest)
        if nest < 0:
            Log.warning(f"May have failed to extract test code for assert in {self.path}\n")
        return before_code + "\n" + after_code
    
    def slice_up(self, code, nest=0):
        """指定した行の上方向にTESTを探索し、}の数をカウントする"""
        lines = code.split("\n")
        for i, line in enumerate(lines[::-1]):
            start_char_count = line.find("{")
            end_char_count = line.find("}")
            nest += start_char_count - end_char_count
            if re.search(r"\bTEST", line):
                return code[len(lines) - i:], nest
        # Log.danger(f"Could not found testcase start code for assert in {self.path}'")
        return code, 1000

    def slice_down(self, code, nest=0):
        """指定した行の下方向に{}を探索する"""
        lines = code.split("\n")
        for i, line in enumerate(lines):
            start_char_count = line.find("{")
            end_char_count = line.find("}")
            nest += start_char_count - end_char_count
            if nest <= 0:
                return code[:i], nest
        # Log.warning(f"Could not found testcase end code for assert in {self.path}'")
        return code, -1