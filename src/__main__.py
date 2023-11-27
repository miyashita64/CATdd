"""CATddのmainファイル

引数として受け取ったコマンドに応じた処理を呼び出す.
ex) $ python -B src コマンド
"""

import sys
from common.catdd_info import CATddInfo
from common.log import Log
from action.tester import Tester

def init():
    """初期化に必要な処理"""
    CATddInfo.load()

def usage():
    """使い方表示"""
    usage_strs = {
        "usage": "show CATdd usage",
        "test": "test target project",
    }
    for command in usage_strs:
        Log.info(command, end="")
        Log.log(f": {usage_strs[command]}")

def test():
    """テスト実行"""
    tester = Tester()
    test_result = tester.test()
    for testcase in test_result.testcase_results:
        if not testcase.is_passed:
            Log.log(testcase.stdout)

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
        "test": test,
    }
    if command in actions:
        try:
            init()
            # コマンドに応じた処理を実行
            actions[command]()
        finally:
            Log.save()
    else:
        if command != "usage":
            # 未定義のコマンドの場合は処理を終了
            Log.danger(f"'{command}' is not defined.")
        # 使い方を表示
        usage()
