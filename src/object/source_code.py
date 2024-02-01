import re
from common.file_interface import FileInterface

class SourceCode:
    def __init__(self, path, code=""):
        # LLMにパスを聞いた際に「何かしらの説明文:　`パス`」と出力された場合の対処
        self.path = FileInterface.parse_path(path)
        if self.path != "" and code == "":
            self._code = FileInterface.read(self.path)
        else:
            self._code = code
        self._code = self.sub_needless_line_code(self._code)

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
        """ファイル書き出し."""
        FileInterface.write(self.path, self._code)

    def copy(self):
        """自身と同じメンバ変数を持つSourceCodeを返す."""
        copy_source_code = SourceCode(self.path, self._code)
        return copy_source_code

    def sub_needless_line_code(self, code):
        """不要な行を削除する."""
        # 不要な行を定義
        needless_pattern_texts = [r"^```cpp$", r"^```CPP$", r"^```Cpp$", r"^```c\+\+$", r"^```C\+\+$", r"^```$", r"\s*###.+"]
        # コードの開始と終了記号を定義
        code_start_pattern = "|".join([r"^```cpp$", r"^```CPP$", r"^```Cpp$", r"^```c\+\+$", r"^```C\+\+$"])
        code_end_pattern = "|".join([r"^```$"])
        # 開始終了記号間のコードを抜き出す
        code_range_pattern = re.compile(f"({code_start_pattern})(?P<code>.*?)({code_end_pattern})", re.DOTALL | re.MULTILINE)
        match = re.search(code_range_pattern, code)
        if match:
            code = match.group("code")

        # 不要な要素を削除
        for pattern_text in needless_pattern_texts:
            pattern = re.compile(pattern_text, re.MULTILINE)
            code = re.sub(pattern, "", code)
        return code
