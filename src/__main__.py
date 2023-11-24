import sys

def usage():
    usage_str = "usage: show CATdd usage"
    print(usage_str)

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
    }
    # コマンドに応じた処理を実行
    if command in actions:
        actions[command]()
    # 未定義のコマンドの場合は処理を終了
    else:
        print(f"'{command}' is not defined.")