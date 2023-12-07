import re
from common.log import Log
from common.file_interface import FileInterface

class SourceCode:
    def __init__(self, path, code=""):
        self.path = path
        if self.path != "" and code == "":
            self._code = FileInterface.read(self.path)
        else:
            self._code = code
        self._code = self.sub_needless_line_code(code)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = self.sub_needless_line_code(code)

    @property
    def lines(self):
        return self._code.split("\n")

    def save(self):
        """ファイル書き出し"""
        Log.info(f"write source code to \"{self.path}\"")
        FileInterface.write(self.path, self._code)

    def copy(self):
        """自身と同じメンバ変数を持つSourceCodeを返す"""
        copy_source_code = SourceCode(self.path, self._code)
        return copy_source_code

    def sub_needless_line_code(self, code):
        """不要な行を削除する"""
        needless_head_pattern = re.compile(r"^```cpp$", re.MULTILINE)
        needless_tail_pattern = re.compile(r"^```$", re.MULTILINE)
        code = re.sub(needless_head_pattern, "", code)
        code = re.sub(needless_tail_pattern, "", code)
        return code