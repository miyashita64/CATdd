import os
import yaml

class CATddInfo():
    """CATdd全体で共有する情報を保持するクラス"""
    # CATddのパス(CATdd/)
    catdd_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    version = None              # バージョン
    target_project_path = None  # 支援対象のパス
    test_exec_path = None       # テスト実行パス
    test_exec_cmd = None        # テスト実行コマンド
    program_lang = None         # ソースコード生成時のプログラム言語
    comment_lang = None         # ソースコード生成時のコメント言語

    @classmethod
    def load(cls):
        """CATddの設定ファイルを読み込む"""
        from common.log import Log  # 循環インポートを回避するための苦肉の策
        config_file_path = CATddInfo.path("catdd.yaml")
        Log.log(f"Loading '{config_file_path}' ... ", end="")
        with open(config_file_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        cls.version = config["version"]
        cls.target_project_path = config["target_project"]["path"]
        cls.test_exec_path = config["target_project"]["test_exec_path"]
        cls.test_exec_cmd = config["target_project"]["test_exec_cmd"]
        cls.program_lang = config["target_project"]["program_lang"]
        cls.comment_lang = config["target_project"]["comment_lang"]
        Log.success("Finish!")

    @classmethod
    def path(cls, additional_path):
        """CATddのパスからの相対パスを受け取り絶対パスを返す"""
        return os.path.normpath(os.path.join(CATddInfo.catdd_path, additional_path))