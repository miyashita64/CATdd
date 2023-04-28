"""ファイル仲介モジュール"""

import re
import os

class FileInterface:
    @staticmethod
    def read(path):
        """指定したファイルのテキストを返す関数"""
        try:
            with open(path, 'r') as f:
                text = f.read().strip()
        except FileNotFoundError:
            text = ""
        return text

    @staticmethod
    def write(path, text):
        """指定したファイルに指定されたテキストを書き込む関数"""
        try:
            with open(path, 'w') as f:
                f.write(text)
        except FileNotFoundError:
            with open(path, 'x') as f:
                f.write(text)

    @staticmethod
    def search(target_name, orgin_dir):
        """指定した名前のファイルを指定したディレクトリから探索し、そのパスを返す関数"""
        for root, dirs, files in os.walk(orgin_dir):
            if target_name in files:
                return os.path.join(root, target_name)
        return None  # ファイルが見つからなかった場合はNoneを返す

    @staticmethod
    def compress(text):
        """文字列を短くする関数"""
        # 連続した記号の排除
        pattern = re.compile(r'([^a-zA-Z0-9\s])\1+')
        non_double_symbol = pattern.sub(r'\1', text)
        # 空行の排除
        lines = non_double_symbol.split("\n")
        non_blank_lines = [line for line in lines if line.strip() != ""]
        return "\n".join(non_blank_lines)

    @staticmethod
    def head_slice(text, max_chars):
        """指定した文字数以上の場合、先頭を優先して返す関数"""
        return text if len(text) < max_chars else text[:max_chars]

    @staticmethod
    def tail_slice(text, max_chars):
        """指定した文字数以上の場合、末尾を優先して返す関数"""
        return text if len(text) < max_chars else text[-max_chars:]