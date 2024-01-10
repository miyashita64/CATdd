# CMake generated Testfile for 
# Source directory: /home/taki/CATdd/target_project/exp3
# Build directory: /home/taki/CATdd/target_project/exp3/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test1 "tdd_sample_test")
set_tests_properties(test1 PROPERTIES  _BACKTRACE_TRIPLES "/home/taki/CATdd/target_project/exp3/CMakeLists.txt;87;add_test;/home/taki/CATdd/target_project/exp3/CMakeLists.txt;0;")
subdirs("googletest-build")
