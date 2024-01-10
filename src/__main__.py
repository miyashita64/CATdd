"""CATddのmainファイル

引数として受け取ったアクションに応じた処理を呼び出す.
ex) $ python -B src アクション
"""

import sys
import time
from common.catdd_info import CATddInfo
from common.log import Log
from common.interpreter import Interpreter
from common.difference import Difference
from action.tester import Tester
from action.source_code_generator import SourceCodeGenerator
from action.base_tester import BaseTester
from object.source_code import SourceCode

def init():
    """初期化に必要な処理"""
    CATddInfo.load()

def usage():
    """使い方表示アクション"""
    # テキスト設定
    action_usage_strs = {
        "usage": "show CATdd usage",
        "test":  "test target project",
        "gen":   "generate source code that may pass the test",
        "base":  "check source code is based on test cases",
    }
    # 表示
    Log.log("CATdd Usage: make [ACTION]\n")
    Log.log("available actions:")
    for action in action_usage_strs:
        Log.info(f"  - {action.ljust(8)} ", end="")
        Log.log(f"{action_usage_strs[action]}")
    Log.log("")

def test():
    """テスト実行アクション"""
    Log.log("Run test ... ")
    # テスト実行
    tester = Tester()
    test_result = tester.test()
    # テスト結果の表示
    test_result.print()
    # テストをパスできなかった場合
    if not test_result.is_passed:
        # ソースコード生成の実行確認
        do_gen = Interpreter.yn("Do generate to fix source code by catdd?")
        if do_gen:
            # ソースコード生成
            generate_source_code(test_result)

def base_test():
    """ソースコードがテストに基づくか検証するアクション"""
    # テスト実行
    Log.log("Run base test ... ")
    base_tester = BaseTester()
    base_tester.all_test()
    Log.log("Complete base testing.\n")

def generate_source_code(test_result=None):
    """ソースコード生成アクション"""
    tester = Tester()
    if test_result is None:
        # テスト実行
        Log.log("Run test ... ")
        test_result = tester.test()
        test_result.print()
        Log.log("Complete testing.\n")

    # ソースコード生成
    Log.log("Generate source code ... ")
    generator = SourceCodeGenerator()
    source_codes = generator.generate(test_result)
    # 生成前のソースコードを保持
    # TODO: 再生成を選んだ場合、ここで再度ソースコードを取得しなおすため
    #       再生成前のソースコードとの差分しか base test を実行できない
    existed_source_codes = [SourceCode(source_code.path) for source_code in source_codes]
    # ソースコード書き込み
    for source_code in source_codes:
        Log.info(f"write source code to \"{source_code.path}\"")
        source_code.save()
    Log.log("Complete source code generation.\n")

    # 生成したソースコードについてテスト
    # do_test = Interpreter.yn("Do test it?")
    do_test = True # ソースコード生成後はテストを自動的に実行する
    if do_test:
        # テスト実行
        Log.log("Run test ... ")
        test_result = tester.test()
        test_result.print()
        # すべてのテストにパスした場合
        if test_result.is_passed:
            # テストに基づいているかテスト
            do_base_test = Interpreter.yn("Do base test it?")
            # do_base_test = False
            if do_base_test:
                base_tester = BaseTester()
                # 変更された各ファイルごとに行う
                for index in range(len(source_codes)):
                    Log.log(f"Check \"{source_codes[index].path}\" based on the test.")
                    source_code_lines = source_codes[index].lines
                    existed_source_code_lines = existed_source_codes[index].lines
                    # 生成前後のソースコードの差を検出
                    diff = Difference(existed_source_code_lines, source_code_lines)
                    # 差の範囲について処理を行う
                    base_tester.test_by_ranges(source_codes[index].copy(), diff.ranges())
        # テストが通らない場合、再度生成する
        else:
            do_regenerate = Interpreter.yn("Re genrate source code?")
            if do_regenerate:
                generate_source_code(test_result)


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
        "base": base_test,
        "generate": generate_source_code,
    }
    if action in actions:
        # 処理開始
        Log.info(f"\nCATdd START [{action}]\n")
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
