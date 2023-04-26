# 自身(Makefile)があるディレクトリの絶対パス
MAKEFILE_DIR/ := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
# CATddのメインファイルのパス
MAIN_SOURCE_PATH := ${MAKEFILE_DIR/}src/__main__.py

# 実行時刻
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

make := make --no-print-directory

# 設定ファイルのパス
SETTING_FILE_PATH := ${MAKEFILE_DIR/}catdd.yaml

# yqを使用して、設定ファイルから値を読み込む
VERSION := $(shell yq -r '.version' ${SETTING_FILE_PATH})
TARGET_PROJECT_PATH := ${MAKEFILE_DIR/}$(shell yq -r '.target_project.path' ${SETTING_FILE_PATH})
TARGET_TEST_CMD := $(shell yq -r '.target_project.test_exec_cmd' ${SETTING_FILE_PATH})
TARGET_TEST_LOG_DIR := ${MAKEFILE_DIR/}$(shell yq -r '.target_project.test_log_dir' ${SETTING_FILE_PATH})
TARGET_TEST_LOG_NAME := $(shell yq -r '.target_project.test_log_name' ${SETTING_FILE_PATH})
PROGRAM_LANG := $(shell yq -r '.target_project.program_lang' ${SETTING_FILE_PATH})
COMMENT_LANG := $(shell yq -r '.target_project.comment_lang' ${SETTING_FILE_PATH})

usage:
	@echo "Please input argument."
	@echo "  run : run CATdd"
	@echo " test : run test for target_project"

run:
	@${make} test_log
	@python3 ${MAIN_SOURCE_PATH}

test:
	@cd ${TARGET_PROJECT_PATH} && ${TARGET_TEST_CMD}

test_log:
	@${make} test 1> ${TARGET_TEST_LOG_DIR}/${TARGET_TEST_LOG_NAME} 2> /dev/null || :
	@cp ${TARGET_TEST_LOG_DIR}/${TARGET_TEST_LOG_NAME} ${TARGET_TEST_LOG_DIR}/${TIMESTAMP}.log

clean:
	@rm ${TARGET_TEST_LOG_DIR}/*