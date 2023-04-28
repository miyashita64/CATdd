from enum import Enum
from gpt_interface import GPTInterface

class GenType(Enum):
    header = 0
    source = 1

class SourceCodeGenerator:
    @staticmethod
    def generate(gen_type, class_name, prg_lang, cmt_lang, source_code, header_code, failed_testcases):
        # 最大トークン数
        max_tokens = 2700
        # プロンプトの構成要素の集合
        cmd_switch = {"main", f"only_{gen_type.name}", "pass_test"}
        sub_switch = set()
        if source_code != "":
            cmd_switch.add("based_source")
        if header_code != "":
            cmd_switch.add("based_header")
        # 削除していく順序
        another = GenType(1-gen_type.value)
        diff_cmds = [set(), {f"based_{another.name}"}, {f"based_{another.name}", f"based_{gen_type.name}"}]
        diff_subs = [set(), {f"based_{another.name}"}, {f"based_{another.name}", f"based_{gen_type.name}"},
                     {f"based_{another.name}", f"based_{gen_type.name}", "test"}]

        # max_tokensを超えないpromptを生成する
        for diff_cmd in diff_cmds:
            for diff_sub in diff_subs:
                dc = diff_cmd
                ds = diff_sub
                if "test" in ds:
                    for count in range(len(failed_testcases), 0, -1):
                        # promptの作成
                        prompt = SourceCodeGenerator.make_prompt(
                            cmd_switch-dc, sub_switch-ds, count,
                            class_name, prg_lang, cmt_lang,
                            source_code, header_code, failed_testcases)
                        if GPTInterface.count_tokens(prompt) < max_tokens:
                            break
                else:
                    prompt = SourceCodeGenerator.make_prompt(
                        cmd_switch-dc, sub_switch-ds, len(failed_testcases),
                        class_name, prg_lang, cmt_lang,
                        source_code, header_code, failed_testcases)
                if GPTInterface.count_tokens(prompt) < max_tokens:
                    break
            if GPTInterface.count_tokens(prompt) < max_tokens:
                break
        # ソースコード生成
        if GPTInterface.count_tokens(prompt) < max_tokens:
            generated_source_code = GPTInterface.request(prompt)
            return generated_source_code
        else:
            print("!!! Test case is too long. !!!")
            return source_code

    @staticmethod
    def make_prompt(cmd_switch, sub_switch, testcase_countor, class_name, prg_lang, cmt_lang, source_code, header_code, failed_testcases):
        cmds = {
            "main": f"Implement the source code for class '{class_name}' that satisfies the following conditions"\
                    f" using {prg_lang} with '{cmt_lang}' comments.\n",
            "only_header" : " - Of the two files, header file and source file, only the header file should be implemented.\n",
            "only_source" : " - Of the two, header file and source file, only the source file should be implemented.\n",
            "pass_test"   : "\n - Satisfy all of the following test cases.\n\n",
            "based_source": "\n - Based on the following source code.\n\n",
            "based_header": "\n - Based on the following header file.\n\n",
        }

        prompt = ""
        for key in cmds:
            if key in cmd_switch:
                # cmdを追加
                prompt += cmds[key]
                # 各ファイルの内容を追加
                if key == "pass_test":
                    prompt += "\n".join(failed_testcases[:testcase_countor])
                elif key in {"based_source", "based_header"}:
                    code = source_code if key=="based_source" else header_code
                    if key in sub_switch:
                        prompt += GPTInterface.sub_japanese(code)
                    else:
                        prompt += code
                prompt += "\n"
        return prompt