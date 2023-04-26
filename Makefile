# 自身(Makefile)があるディレクトリの絶対パス
MAKEFILE_PATH = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
MAIN_SOURCE_PATH = ${MAKEFILE_PATH}src/__main__.py

# 実行時刻
TIMESTAMP = $(shell date +%Y%m%d%H%M%S)

make = make --no-print-directory

usage:
	@echo "Please input argument."
	@echo " run : run CATdd"

run:
	@python3 ${MAIN_SOURCE_PATH}