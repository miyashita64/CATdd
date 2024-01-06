"""ファイル仲介モジュール"""

import re
import os
from common.log import Log

class FileInterface:
    @staticmethod
    def read(path):
        """指定したファイルのテキストを返す関数"""
        try:
            with open(path, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            text = ""
        finally:
            return text

    @staticmethod
    def write(path, text):
        """指定したファイルに指定されたテキストを書き込む関数"""
        with open(path, 'w') as f:
            f.write(text)

    @staticmethod
    def search(target_file_name, dir_path):
        """指定した名前のファイルを指定したディレクトリから探索し、そのパスを返す関数"""
        for root, dirs, files in os.walk(dir_path):
            if target_file_name in files:
                return os.path.join(root, target_file_name)
        Log.warning(f"\"{target_file_name}\" is not found in {dir_path}")
        return None  # ファイルが見つからなかった場合はNoneを返す

    @staticmethod
    def search_all(pattern, dir_path):
        """指定した名前のファイルを指定したディレクトリから探索し、そのパスを返す関数"""
        file_paths = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if re.match(pattern, file):
                    file_paths.append(os.path.join(root, file))
        return file_paths

    @staticmethod
    def parse_path(path):
        """LLMなどが出力するパスから余計なものを削除する関数"""
        match = re.search(r'`([^`]+)`', path)
        if match:
            path = match.group(1)
        if len(path.split(":")) > 1:
            path = path.split(":")[-1]
        return path.replace("\n", "").replace("`", "")
        