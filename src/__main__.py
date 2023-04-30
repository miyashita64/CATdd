# 標準・外部
import yaml
# 共通モジュール
from file_interface import FileInterface
# 処理部
from result_analyzer import ResultAnalyzer
from testcase_analyzer import TestcaseAnalyzer
from source_code_generator import SourceCodeGenerator, GenType

def main():
    print("\n[CATdd START]\n")
    # YAMLファイルの読み取り
    print("Loading 'catdd.yaml' ... ", end="")
    with open('catdd.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    print("Finish!")

    # テスト結果解析
    print("Analyzing test results ... ", end="")
    log_path = f"{config['target_project']['test_log_dir']}/{config['target_project']['test_log_name']}"
    failed_test_datas = ResultAnalyzer.analyze(log_path)
    print("Finish!")

    # テストの失敗を検出できなかった場合
    if len(failed_test_datas) == 0:
        print("Already passed all tests!")
    # 失敗した各テストについて
    for test_data in failed_test_datas:
        # 失敗したテストケースが対象とするクラス名
        class_name = test_data["path"].split("/")[-1].split("Test.")[0].split(".")[0]
        # 失敗したテストケースを一覧表示
        print(f"\nClass {class_name} did not pass the test.")
        for label in test_data["labels"]:
            print(f"  - {label}")

        # 失敗したテストケースの内容を抽出する
        print(f"\nTracking failed test cases for {class_name} ... ", end="")
        failed_testcases = TestcaseAnalyzer.analyze(test_data)
        print("Finish!")
        
        # 失敗したテストケースが対象とするクラスのソースコード
        header_file_path = FileInterface.search(f"{class_name}.h", config["target_project"]["src_dir"])
        source_file_path = FileInterface.search(f"{class_name}.cpp", config["target_project"]["src_dir"])
        if header_file_path is None:
            header_file_path = f"{config['target_project']['src_dir']}/{class_name}.h"
        else:
            if source_file_path is None:
                source_file_path = f"{header_file_path[:-2]}.cpp"
        if source_file_path is None:
            source_file_path = f"{config['target_project']['src_dir']}/{class_name}.cpp"
        # ヘッダーファイルの読み込み
        header_code = FileInterface.read(header_file_path)
        # ソースコードの読み込み
        source_code = FileInterface.read(source_file_path)

        # ソースコード生成
        # ヘッダファイル生成
        print("Generating header code ... ", end="")
        generated_header_code = SourceCodeGenerator.generate(
            GenType.header,
            class_name,
            config["target_project"]["program_lang"],
            config["target_project"]["comment_lang"],
            source_code,
            header_code,
            failed_testcases,
        )
        print("Finish!")
        # ソースファイル生成
        print("Generating source code ... ", end="")
        generated_source_code = SourceCodeGenerator.generate(
            GenType.source,
            class_name,
            config["target_project"]["program_lang"],
            config["target_project"]["comment_lang"],
            source_code,
            generated_header_code,
            failed_testcases,
        )
        print("Finish!")

        # ヘッダーファイル書き込み
        if header_code == "":
            print(f"Writing header code to {header_file_path} ... ", end="")
            FileInterface.write(header_file_path, generated_header_code)
            print("Finish!")
        # ソースファイル書き込み
        print(f"Writing source code to {source_file_path} ... ", end="")
        FileInterface.write(source_file_path, generated_source_code)
        print("Finish!")
    print("\n[CATdd COMPLETED]\n")

if __name__ == "__main__":
    main()