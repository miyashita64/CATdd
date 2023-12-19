import tiktoken
from enum import Enum

class Priority(Enum):
    GEN = 5
    BASE = 3
    ANOTOHER = 2
    FIRST_RESULT = 4
    RESULT = 1

class Prompt:
    def __init__(self, elms, max_token):
        self.elms = elms
        self.max_token = max_token
        self.value = self.join_elms()

    def join_elms(self):
        while self.calc_total_token() > self.max_token:
            for elm in self.elms:
                elm.priority -= 1
        return "\n".join([elm.value for elm in self.elms])

    def calc_total_token(self):
        return sum([elm.token for elm in self.elms])

class GeneratePassableCodePrompt(Prompt):
    """テストにパスできるソースコードを生成するためのプロンプト"""
    def __init__(self, class_name, is_header_type, failed_testcase_results, header_code, source_code):
        file_type = "header" if is_header_type else "source"
        file_type_extension = ".h" if is_header_type else ".cpp"
        file_type_code = header_code if is_header_type else source_code
        failed_testcase_elms = [PromptElement(
                    f"{testcase_result.code}\n{testcase_result.stdout}\n",
                    Priority.FIRST_RESULT.value if testcase_result is failed_testcase_results[0] else Priority.RESULT.value
                ) for testcase_result in failed_testcase_results]
        passable_elms = [
            PromptElement(f"Implement a {file_type} file that will pass the following test cases.\n" \
                        + f"However, only the {file_type} file out of the two files, source file and header file. Please return code only.\n" \
                        + f"\n### Failed test cases to pass:\n", Priority.GEN.value),
            *failed_testcase_elms,
            PromptElement(f"\n### {file_type} file (base code \"{class_name}.{file_type_extension}\"):\n" \
                        + f"{file_type_code}\n", Priority.BASE.value)
        ]
        if not is_header_type:
            another_type = "source" if is_header_type else "header"
            another_type_extension = ".cpp" if is_header_type else ".h"
            another_type_code = source_code if is_header_type else header_code
            passable_elms += [
                PromptElement(f"\n### {another_type} file (\"{class_name}.{another_type_extension}\"):\n{another_type_code}\n", Priority.ANOTOHER.value)
            ]
        super().__init__(passable_elms, 4096 * 0.5) # 4096 = GPT-3.5-turboの最大の入出力トークン数

class GenerateTestableCodePrompt(Prompt):
    """テストにパスできるソースコードを生成するためのプロンプト"""
    def __init__(self, class_name, is_header_type, error, test_code, header_code, source_code):
        file_type = "header" if is_header_type else "source"
        file_type_extension = ".h" if is_header_type else ".cpp"
        file_type_code = header_code if is_header_type else source_code
        testable_elms = [
            PromptElement(f"Implement a {file_type} file that resolve the following errors.\n" \
                        + f"Only the {file_type} file out of the two files, source file and header file. Please return code only.\n" \
                        + f"\n### Error:\n{error}", Priority.GEN.value),
            PromptElement(f"\n### However, the code should pass the following tests:\n{test_code}\n", Priority.RESULT.value),
            PromptElement(f"\n### {file_type} file (base code \"{class_name}.{file_type_extension}\"):\n" \
                        + f"{file_type_code}\n", Priority.BASE.value)
        ]
        if not is_header_type:
            another_type = "source" if is_header_type else "header"
            another_type_extension = ".cpp" if is_header_type else ".h"
            another_type_code = source_code if is_header_type else header_code
            testable_elms += [
                PromptElement(f"\n### {another_type} file (\"{class_name}.{another_type_extension}\"):\n{another_type_code}\n", Priority.ANOTOHER.value)
            ]
        super().__init__(testable_elms, 4096 * 0.5) # 4096 = GPT-3.5-turboの最大の入出力トークン数

class PromptElement:
    def __init__(self, value, priority=0):
        self.priority = priority if value != "" else -1
        self._value = value
        self._token = self.calc_token()

    @property
    def value(self):
        return self._value if self.priority > 0 else ""

    @property
    def token(self):
        return self._token if self.priority > 0 else 0

    def calc_token(self):
        # トークン数を算出する
        encoding_35 = tiktoken.encoding_for_model("gpt-3.5-turbo-0301")
        encoding = tiktoken.get_encoding(encoding_35.name)
        num_tokens = len(encoding.encode(self.value))
        return num_tokens
