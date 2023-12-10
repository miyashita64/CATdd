from difflib import SequenceMatcher
from common.log import Log


class Difference:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.matcher = SequenceMatcher(None, self.seq1, self.seq2)
        self.opcodes = self.matcher.get_opcodes()

    def print(self):
        # 操作のリストを表示
        Log.log("=== opcodes ===")
        for tag, i1, i2, j1, j2 in self.opcodes:
            Log.log(f"{tag} a[{i1}:{i2}] b[{j1}:{j2}]")
        # 実際の差分を表示
        Log.log("\n=== Differences ===")
        for tag, i1, i2, j1, j2 in self.opcodes:
            if tag == 'delete':
                Log.log(f"Delete from a[{i1}:{i2}]: {self.seq1[i1:i2]}")
            elif tag == 'insert':
                Log.log(f"Insert into b[{j1}:{j2}]: {self.seq2[j1:j2]}")
            elif tag == 'replace':
                Log.log(f"Replace a[{i1}:{i2}] with b[{j1}:{j2}]: {self.seq1[i1:i2]} -> {self.seq2[j1:j2]}")
