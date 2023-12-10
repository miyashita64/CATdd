from tqdm import tqdm
from common.catdd_info import CATddInfo
from common.log import Log
from common.file_interface import FileInterface
from action.tester import Tester
from object.source_code import SourceCode

class BaseTester:
    def all_test(self):
        tester = Tester()
        target_file_pattern = r".*\.cpp$"
        target_file_paths = FileInterface.search_all(target_file_pattern, CATddInfo.src_path)
        for file_path in target_file_paths:
            Log.log(f"Check \"{file_path}\"")
            original_source_code = SourceCode(file_path)
            needless_line_logs = ""
            try:
                # 各行についてテストのパスに必要か検証する
                for line_num in tqdm(range(len(original_source_code.lines))):
                    source_code = original_source_code.copy()
                    lines = source_code.lines.copy()
                    delete_line = lines[line_num]
                    none_space_chars = delete_line.strip()
                    # 空行や{}だけの行、コメントと思われる行はスキップ
                    if len(none_space_chars) < 4 or none_space_chars[0] == "/":
                        continue
                    # 各行の有無がテスト結果に影響するかを検証する
                    new_lines = self.gen_line_by_sub_element(delete_line)
                    # 削除する行を構成要素が異なる行に書き換える
                    for new_line in tqdm(new_lines):
                        # 生成した行を元のソースコードに埋め込み
                        lines[line_num] = new_line
                        source_code.code = "\n".join(lines)
                        source_code.save()
                        # テスト実行
                        test_result = tester.test()
                        # 指定した要素について、不要と思われる記述があった場合
                        if test_result.is_passed:
                            needless_line_logs += f"{file_path}:{line_num+1} seems not to be based on test cases. \n{delete_line}\n\n"
                    # 指定した行について、不要と思われる記述があった場合
                    if needless_line_logs != "":
                        Log.warning(f"The following lines are not required to pass the test.\n{needless_line_logs}")
            except Exception as e:
                Log.danger(e)
            finally:
                # 元のファイルに戻す
                original_source_code.save()

    def gen_line_by_sub_element(self, delete_line):
        # 複合条件や引数を考慮する
        for keyword in ["&&", "||", "("]:
            delete_line = delete_line.replace(keyword, f"{keyword}\n")
        for keyword in [","]:
            delete_line = delete_line.replace(keyword, f"{keyword} \n")
        for keyword in [")"]:
            delete_line = delete_line.replace(keyword, f"\n{keyword}\n")
        # 各要素を行に分割する
        delete_line_parts = delete_line.split("\n")
        print(delete_line_parts)

        # 各要素ごとにその有無がことなる行を生成する
        new_lines = [""]    # 行を丸ごと削除するため""の要素を含める
        for part_num in range(len(delete_line_parts)):
            # '('や')'でテストを行ってしまうのを回避
            if len(delete_line_parts[part_num]) < 4:
                continue
            parts = delete_line_parts.copy()
            # 削除する要素が複合条件や複数の引数の途中の末尾の要素であった場合、
            # 直前の接続詞(&&や||など)を削除する必要がある
            if parts[part_num][-2:] not in [", ", "&&", "||"]:
                pre_part = parts[part_num-1] if part_num > 0 else ""
                if pre_part[-2:] in [", ", "&&", "||"]:
                    # 直前の接続詞を削除
                    parts[part_num-1] = parts[part_num-1][:-2]
            # 指定要素を削除した行を生成
            parts.pop(part_num)
            new_line = "".join(parts)
            new_lines += [new_line]
        return new_lines
