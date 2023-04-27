# 自身(Makefile)があるディレクトリの絶対パス
MAKEFILE_DIR/ := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
# CATddのメインファイルのパス
MAIN_SOURCE_PATH := ${MAKEFILE_DIR/}src/__main__.py

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

# make実行時にディレクトリを表示しない
make := make --no-print-directory
# 実行時刻
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

usage:
	@echo "Please input argument."
	@echo "      run : run CATdd"
	@echo "     test : run test for target_project"
	@echo " test_log : run & log test for target_project"
	@echo "    clean : delete logs of test for target_project"

run:
	@${make} test_log
	@python3 -B ${MAIN_SOURCE_PATH}

test:
	@cd ${TARGET_PROJECT_PATH} && ${TARGET_TEST_CMD}

test_log:
	@echo -n "Testing ... "
	@${make} test > ${TARGET_TEST_LOG_DIR}/${TARGET_TEST_LOG_NAME} 2>&1 || :
	@cp ${TARGET_TEST_LOG_DIR}/${TARGET_TEST_LOG_NAME} ${TARGET_TEST_LOG_DIR}/${TIMESTAMP}.log
	@echo Finish!

clean:
	@rm ${TARGET_TEST_LOG_DIR}/*