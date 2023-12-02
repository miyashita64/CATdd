from common.log import Log

class SourceCode:
    def __init__(self, path, code):
        self.path = path
        self.code = code
        self.lines = code.split("\n")

    def save(self):
        """ファイル書き出し"""
        Log.info(f"write source code to \"{self.path}\"")
        with open(self.path, mode="w") as f:
            f.write(self.code)