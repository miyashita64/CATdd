mkfile_path := $(dir $(lastword $(MAKEFILE_LIST)))

APPL_COBJS +=

SRCLANG := c++

ifdef CONFIG_EV3RT_APPLICATION

# Include libraries
include $(EV3RT_SDK_LIB_DIR)/libcpp-ev3/Makefile

endif

# ソースコードのあるディレクトリを指定する？
APPL_DIRS += \
    $(mkfile_path)module

# ヘッダファイルのあるディレクトリを指定する？
INCLUDES += \
    -I$(mkfile_path)module

COPTS += -std=gnu++11