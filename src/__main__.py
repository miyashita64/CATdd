import yaml
from result_analyzer import ResultAnalyzer
from testcase_analyzer import TestcaseAnalyzer
from file_interface import FileInterface
from gpt_interface import GPTInterface

def main():
    # YAMLファイルの読み取り
    with open('catdd.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    # テスト結果解析
    log_path = f"{config['target_project']['test_log_dir']}/{config['target_project']['test_log_name']}"
    failed_test_datas = ResultAnalyzer.analyze(log_path)
    # 失敗した各テストケースを収集する
    for test_data in failed_test_datas:
        # 失敗したテストケースの内容を抽出する
        failed_testcases = TestcaseAnalyzer.analyze(test_data)
        faild_testcode = "".join(failed_testcases)
        # 失敗したテストケースが対象とするクラス名
        class_name = test_data["path"].split("/")[-1].split("Test.")[0]
        # 失敗したテストケースが対象とするクラスのソースコード
        source_code_path = FileInterface.search(f"{class_name}.cpp", config["target_project"]["src_dir"])
        header_path = FileInterface.search(f"{class_name}.h", config["target_project"]["src_dir"])
        source_code = FileInterface.read(source_code_path)
        header_code = FileInterface.read(header_path)
        # # ソースコード生成
        # prompt = f"Implement class {class_name}, which should pass the test by the following test case, in {config['target_project']['program_lang']} with {config['target_project']['comment_lang']} comments."
        # prompt += faild_testcode
        # print(GPTInterface.request(prompt))
        # ソースコード生成
        prompt = f"Please rewrite the following file {class_name}.cpp so that the test with the following test case passes."
        prompt += source_code
        prompt += "\n\nBelow is a testcase.\n\n"
        prompt += faild_testcode
        generated_source_code = GPTInterface.request(prompt)
        FileInterface.write(source_code_path, generated_source_code)

if __name__ == "__main__":
    main()