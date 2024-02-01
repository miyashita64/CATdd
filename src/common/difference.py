from difflib import SequenceMatcher
from common.log import Log

class Difference:
    """文字列の差分を保持するクラス."""
    def __init__(self, before_text, after_text):
        self.before_text = before_text
        self.after_text = after_text
        self.matcher = SequenceMatcher(None, self.before_text, self.after_text)
        self.opcodes = self.matcher.get_opcodes()

    def ranges(self):
        """差分(equalでない部分)の行数の範囲を返す."""
        ranges = []
        for tag, _, _, after_start, after_end in self.opcodes:
            if tag != "equal":
                ranges += [range(after_start, after_end)]
        return ranges