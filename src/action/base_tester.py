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
            original_source_code = SourceCode(file_path)
            try:
                for line_num in range(len(original_source_code.lines)):
                    source_code = original_source_code.copy()
                    delete_line = source_code.lines.pop(line_num)
                    none_space_chars = delete_line.strip()
                    if len(none_space_chars) < 4 or none_space_chars[0] == "/":
                        # 空行や{}だけの行、コメントと思われる行はスキップ
                        continue
                    source_code.code = "\n".join(source_code.lines)
                    source_code.save()
                    test_result = tester.test()
                    if test_result.is_passed:
                        Log.warning(f"{file_path}:{line_num} seems not to be based on test cases. \n{delete_line}\n")
            except Exception as e:
                Log.danger(e)
            finally:
                # 元のファイルに戻す
                original_source_code.save()
