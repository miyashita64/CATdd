"""CATddのmainファイル

引数として受け取ったコマンドに応じた処理を呼び出す.
ex) $ python -B src コマンド
"""

import sys
import yaml
from action.tester import Tester

def load_catdd_config():
    """CATddの設定ファイルを読み込む"""
    config_file_path = "catdd.yaml"
    print(f"Loading '{config_file_path}' ... ", end="")
    with open('catdd.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    print("Finish!")
    return config

def usage():
    """使い方表示"""
    usage_str = "usage: show CATdd usage"
    print(usage_str)

def test():
    """テスト実行"""
    config = load_catdd_config()
    test_exec_path = config["target_project"]["test_exec_path"]
    test_exec_cmd = config["target_project"]["test_exec_cmd"]
    tester = Tester(test_exec_path, test_exec_cmd)
    test_result = tester.test()
    for testcase in test_result.testcase_results:
        if not testcase.is_passed:
            print(testcase.stdout)

if __name__ == "__main__":
    """
    引数として受け取ったコマンドに応じた処理を呼び出す.
    ex) $ python -B src コマンド
    """
    args = sys.argv
    # 引数が与えられなかった場合、"usage"(使い方表示コマンド)を設定
    command = args[1] if len(args) >= 2 else "usage"
    # 各コマンドに対して関数を設定
    actions = {
        "usage": usage,
        "test": test,
    }
    if command in actions:
        # コマンドに応じた処理を実行
        actions[command]()
    else:
        # 未定義のコマンドの場合は処理を終了
        print(f"'{command}' is not defined.")