from common.log import Log
from common.file_interface import FileInterface

class SourceCode:
    def __init__(self, path, code=""):
        self.path = path
        if self.path != "" and code == "":
            self.code = FileInterface.read(self.path)
        else:
            self.code = code
        self.lines = self.code.split("\n")

    def save(self):
        """ファイル書き出し"""
        Log.info(f"write source code to \"{self.path}\"")
        FileInterface.write(self.path, self.code)

    def copy(self):
        """自身と同じメンバ変数を持つSourceCodeを返す"""
        copy_source_code = SourceCode(self.path, self.code)
        return copy_source_code
