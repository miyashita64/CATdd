import os
from enum import Enum
from common.catdd_info import CATddInfo

class Color(Enum):
    """各色に対応するエスケープシーケンスの値を管理する辞書"""
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    DEFAULT = 9
    GRAY = 90

class Log:
    """ターミナルやログファイルへの出力を行うクラス"""
    output_path = CATddInfo.path("logs/latest.log")
    log_text = ""

    @classmethod
    def log(cls, text, end="\n"):
        """通常の出力"""
        print(text, end=end)
        cls.log_text += str(text) + end
    
    @classmethod
    def data(cls, text):
        """標準出力はしないがログに記録する"""
        text = f"\n{Log.color_es(Color.GRAY)}{text}{Log.color_es(Color.DEFAULT)}\n"
        cls.log_text += text
    
    @classmethod
    def save(cls):
        """ファイル書き出し"""
        from common.file_interface import FileInterface # 循環インポートを回避するための苦肉の策
        FileInterface.write(cls.output_path, cls.log_text)
        cls.log_text = ""

    """ログのバリエーション"""
    @classmethod
    def info(cls, text, end="\n"):
        """重要情報"""
        info_text = f"{Log.color_es(Color.CYAN)}{text}{Log.color_es(Color.DEFAULT)}"
        cls.log(info_text, end)

    @classmethod
    def success(cls, text, end="\n"):
        """成功や完了"""
        success_text = f"{Log.color_es(Color.GREEN)}{text}{Log.color_es(Color.DEFAULT)}"
        cls.log(success_text, end)

    @classmethod
    def warning(cls, text, end="\n"):
        """警告"""
        warning_text = f"{Log.color_es(Color.YELLOW)}{text}{Log.color_es(Color.DEFAULT)}"
        cls.log(warning_text, end)

    @classmethod
    def danger(cls, text, end="\n"):
        """致命的な事態"""
        danger_text = f"\n{Log.color_es(Color.RED)}!!! {text} !!!{Log.color_es(Color.DEFAULT)}\n"
        cls.log(danger_text, end)

    """エスケープシーケンス"""
    @staticmethod
    def color_es(color: Color):
        """文字色を指定するエスケープシーケンスを返す"""
        if color is Color.GRAY:
            return "\033[90m"
        return f"\033[3{color.value}m"

    @staticmethod
    def bg_color_es(color: Color):
        """文字の背景色を指定するエスケープシーケンスを返す"""
        if color is Color.GRAY:
            return "\033[47m"   # 白だけど
        return f"\033[4{color.value}m"