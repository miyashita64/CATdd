"""ファイル仲介モジュール"""

import re
import os
from common.log import Log

class FileInterface:
    @staticmethod
    def read(path):
        """指定したファイルのテキストを返す関数"""
        try:
            Log.log(f"Reading \"{path}\" ... ", end="")
            with open(path, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            text = ""
        finally:
            Log.success("Finish!")
            return text

    @staticmethod
    def write(path, text):
        """指定したファイルに指定されたテキストを書き込む関数"""
        Log.log(f"Writing \"{path}\" ... ", end="")
        with open(path, 'w') as f:
            f.write(text)
        Log.success("Finish!")

    @staticmethod
    def search(target_file_name, dir_path):
        """指定した名前のファイルを指定したディレクトリから探索し、そのパスを返す関数"""
        Log.log(f"Searching \"{target_file_name}\" from \"{dir_path}\" ... ", end="")
        for root, dirs, files in os.walk(dir_path):
            if target_file_name in files:
                Log.success("Finish!")
                return os.path.join(root, target_file_name)
        Log.warning("Failed!")
        return None  # ファイルが見つからなかった場合はNoneを返す
