# 自身(Makefile)があるディレクトリの絶対パス
MAKEFILE_PATH := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
# CATddのメインファイルのパス
MAIN_SOURCE_PATH := ${MAKEFILE_PATH}src/__main__.py

# 実行時刻
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

# 設定ファイルのパス
SETTING_FILE_PATH := ${MAKEFILE_PATH}catdd.yaml

# yqを使用して、設定ファイルから値を読み込む
VERSION := $(shell yq -r '.version' ${SETTING_FILE_PATH})
TARGET_PROJECT_PATH := ${MAKEFILE_PATH}$(shell yq -r '.target_project.path' ${SETTING_FILE_PATH})
TARGET_TEST_CMD := $(shell yq -r '.target_project.test_exec_cmd' ${SETTING_FILE_PATH})
PROGRAM_LANG := $(shell yq -r '.target_project.program_lang' ${SETTING_FILE_PATH})
COMMENT_LANG := $(shell yq -r '.target_project.comment_lang' ${SETTING_FILE_PATH})

usage:
	@echo "Please input argument."
	@echo "  run : run CATdd"
	@echo " test : run test for target_project"

run:
	@python3 ${MAIN_SOURCE_PATH}

test:
	@cd ${TARGET_PROJECT_PATH} && ${TARGET_TEST_CMD}