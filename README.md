# CATdd
Continuous Automated Test Driven Development.

CATddは、機械学習を用いた自動的なソースコード生成による、テスト駆動開発の継続的な支援を目的としたフレームワークです。

## 実行環境
- Python3.10.6

## 環境設定
CATddを使用するには、catdd.yamlに適切な値を設定する必要があります。
1. target_project/下に、CATddを適用したいプロジェクトを設置する
1. catdd.yamlの各値を設定する
```
version: 1.0
target_project:
  path: target_project/YOUR_PROJECT_PATH
  src_dir: target_project/YOUR_PROJECT_PATH/SOURCE
  test_exec_cmd: YOUR_PROJECT_RUN_TEST_COMMAND_on_YOUR_PROJECT_PATH
  test_log_dir: target_project/logs
  test_log_name: latest.log
  program_lang: C++
  comment_lang: japanese
```