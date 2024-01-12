cmake_minimum_required(VERSION 3.12)

project(googletest-download NONE)

include(ExternalProject)
ExternalProject_Add(googletest
  GIT_REPOSITORY    https://github.com/google/googletest.git
  GIT_TAG           release-1.11.0
  SOURCE_DIR        "/mnt/c/Users/miyashita/Documents/wsl_box/CATdd/target_project/application_example/build/googletest-src"
  BINARY_DIR        "/mnt/c/Users/miyashita/Documents/wsl_box/CATdd/target_project/application_example/build/googletest-build"
  CONFIGURE_COMMAND ""
  BUILD_COMMAND     ""
  INSTALL_COMMAND   ""
  TEST_COMMAND      ""
)
