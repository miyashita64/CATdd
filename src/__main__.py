"""CATddのmainファイル

引数として受け取ったアクションに応じた処理を呼び出す.
ex) $ python -B src アクション
"""

import sys
import time
from common.catdd_info import CATddInfo
from common.log import Log
from action.tester import Tester
from action.source_code_generator import SourceCodeGenerator
from action.base_tester import BaseTester

def init():
    """初期化に必要な処理"""
    CATddInfo.load()

def usage():
    """使い方表示"""
    action_usage_strs = {
        "usage": "show CATdd usage",
        "test":  "test target project",
        "gen":   "generate source code that may pass the test",
        "base":  "check source code is based on test cases",
    }
    Log.log("CATdd Usage: make [ACTION]\n")
    Log.log("available actions:")
    for action in action_usage_strs:
        Log.info(f"  - {action.ljust(8)} ", end="")
        Log.log(f"{action_usage_strs[action]}")
    Log.log("")

def test():
    """テスト実行"""
    tester = Tester()
    test_result = tester.test()
    if test_result.is_passed:
        Log.success("Test all pass!")
    elif test_result.is_exec_test:
        Log.warning("Test failed.")
        for testcase_result in test_result.testcase_results:
            if not testcase_result.is_passed:
                Log.log(testcase_result.stdout)
    else:
        Log.warning("Compoile Error")
        Log.log(test_result.stderr)
    return test_result

def is_based_test():
    """ソースコードがテストケースに基づいているかを判定"""
    base_tester = BaseTester()
    base_tester.all_test()

def source_code_generate():
    """ソースコード生成"""
    tester = Tester()
    test_result = tester.test()
    generator = SourceCodeGenerator()
    source_codes = generator.generate(test_result)
    for source_code in source_codes:
        source_code.save()

if __name__ == "__main__":
    """
    引数として受け取ったアクションに応じた処理を呼び出す.
    ex) $ python -B src アクション
    """
    args = sys.argv
    # 引数が与えられなかった場合、"usage"(使い方表示アクション)を設定
    action = args[1] if len(args) >= 2 else "usage"
    # 各アクションに対して関数を設定
    actions = {
        "test": test,
        "generate": source_code_generate,
        "base": is_based_test,
    }
    if action in actions:
        # 処理開始
        Log.info("\nCATdd START\n")
        # 処理開始時間の記録
        start_time = time.time()
        try:
            init()
            # アクションに応じた処理を実行
            actions[action]()
        except Exception as e:
            Log.danger(f"\n{e}\n")
        finally:
            # 処理時間の計測と整形
            processing_seconds = time.time() - start_time
            minutes, seconds = divmod(processing_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            # 処理時間の表示
            Log.info(f"\nProcessing time: {int(hours):2d}:{int(minutes):02d}:{int(seconds):02d}")
            # 処理終了
            Log.info("\nCATdd COMPLETE\n")
            Log.save()
    else:
        if action != "usage":
            # 未定義のアクションの場合は処理を終了
            Log.danger(f"'{action}' is not defined.")
        # 使い方を表示
        usage()
