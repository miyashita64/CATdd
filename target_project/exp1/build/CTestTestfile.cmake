# CMake generated Testfile for 
# Source directory: /mnt/c/Users/miyashita/Documents/wsl_box/CATdd/target_project/application_example
# Build directory: /mnt/c/Users/miyashita/Documents/wsl_box/CATdd/target_project/application_example/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test1 "tdd_sample_test")
set_tests_properties(test1 PROPERTIES  _BACKTRACE_TRIPLES "/mnt/c/Users/miyashita/Documents/wsl_box/CATdd/target_project/application_example/CMakeLists.txt;87;add_test;/mnt/c/Users/miyashita/Documents/wsl_box/CATdd/target_project/application_example/CMakeLists.txt;0;")
subdirs("googletest-build")
