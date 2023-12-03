import re
from common.log import Log
from common.file_interface import FileInterface

class TestCode:
    """テストコードを保持するクラス"""

    def __init__(self, file_path):
        """コンストラクタ"""
        self.path = file_path
        self.lines = []
        self.code = FileInterface.read(self.path)
        self.lines = self.code.split("\n")

    def slice_testcase(self, row):
        """指定された行を含むテストケースのコードを抽出する"""
        before_code = self.slice_up("\n".join(self.lines[:row]))
        after_code = self.slice_down("\n".join(self.lines[row:]))
        return before_code + "\n" + after_code
    
    def slice_up(self, code, nest=0):
        """指定した行の上方向に{}を探索する"""
        target_text_count = code.rfind("{")
        recursive_text_count = code.rfind("}")
        if target_text_count < 0:
            # 上方向に{がない場合、テストケースが閉じられていないため異常
            Log.danger(f"Could not found testcase start code for assert in {self.file_path}'")
            exit()
        elif target_text_count > recursive_text_count:
            if nest == 0:
                # テストケースの出口を発見
                return code[target_text_count:]
            else:
                # ネスト中の出口を発見
                return self.slice_up(code[:target_text_count], nest-1) + code[target_text_count:]
        else:
            # 出口の前に入口が見つかったため、ネストして再探索
            return self.slice_up(code[:recursive_text_count], nest+1) + code[recursive_text_count:]

    def slice_down(self, code, nest=0):
        """指定した行の下方向に{}を探索する"""
        target_text_count = code.find("}")
        recursive_text_count = code.find("{")
        if target_text_count < 0:
            # 下方向に}がない場合、テストケースが閉じられていないため異常
            Log.danger(f"Could not found testcase end code for assert in {self.file_path}'")
            exit()
        elif recursive_text_count < 0 or target_text_count < recursive_text_count:
            if nest == 0:
                # テストケースの出口を発見
                return code[:target_text_count+1]
            else:
                # ネスト中の出口を発見
                return self.slice_down(code[target_text_count+1:], nest-1) + code[:target_text_count+1]
        else:
            # 出口の前に入口が見つかったため、ネストして再探索
            return self.slice_down(code[recursive_text_count:], nest+1) + code[:recursive_text_count]
