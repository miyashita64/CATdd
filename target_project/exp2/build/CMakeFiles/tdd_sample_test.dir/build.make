# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/taki/CATdd/target_project/exp2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/taki/CATdd/target_project/exp2/build

# Include any dependencies generated for this target.
include CMakeFiles/tdd_sample_test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/tdd_sample_test.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/tdd_sample_test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/tdd_sample_test.dir/flags.make

CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o: CMakeFiles/tdd_sample_test.dir/flags.make
CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o: ../test/TriangleTest.cpp
CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o: CMakeFiles/tdd_sample_test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/taki/CATdd/target_project/exp2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o -MF CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o.d -o CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o -c /home/taki/CATdd/target_project/exp2/test/TriangleTest.cpp

CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/taki/CATdd/target_project/exp2/test/TriangleTest.cpp > CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.i

CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/taki/CATdd/target_project/exp2/test/TriangleTest.cpp -o CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.s

CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o: CMakeFiles/tdd_sample_test.dir/flags.make
CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o: ../module/Triangle.cpp
CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o: CMakeFiles/tdd_sample_test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/taki/CATdd/target_project/exp2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o -MF CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o.d -o CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o -c /home/taki/CATdd/target_project/exp2/module/Triangle.cpp

CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/taki/CATdd/target_project/exp2/module/Triangle.cpp > CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.i

CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/taki/CATdd/target_project/exp2/module/Triangle.cpp -o CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.s

CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o: CMakeFiles/tdd_sample_test.dir/flags.make
CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o: ../module/blank.cpp
CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o: CMakeFiles/tdd_sample_test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/taki/CATdd/target_project/exp2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o -MF CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o.d -o CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o -c /home/taki/CATdd/target_project/exp2/module/blank.cpp

CMakeFiles/tdd_sample_test.dir/module/blank.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tdd_sample_test.dir/module/blank.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/taki/CATdd/target_project/exp2/module/blank.cpp > CMakeFiles/tdd_sample_test.dir/module/blank.cpp.i

CMakeFiles/tdd_sample_test.dir/module/blank.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tdd_sample_test.dir/module/blank.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/taki/CATdd/target_project/exp2/module/blank.cpp -o CMakeFiles/tdd_sample_test.dir/module/blank.cpp.s

# Object files for target tdd_sample_test
tdd_sample_test_OBJECTS = \
"CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o" \
"CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o" \
"CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o"

# External object files for target tdd_sample_test
tdd_sample_test_EXTERNAL_OBJECTS =

tdd_sample_test: CMakeFiles/tdd_sample_test.dir/test/TriangleTest.cpp.o
tdd_sample_test: CMakeFiles/tdd_sample_test.dir/module/Triangle.cpp.o
tdd_sample_test: CMakeFiles/tdd_sample_test.dir/module/blank.cpp.o
tdd_sample_test: CMakeFiles/tdd_sample_test.dir/build.make
tdd_sample_test: lib/libgtest_main.a
tdd_sample_test: lib/libgtest.a
tdd_sample_test: CMakeFiles/tdd_sample_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/taki/CATdd/target_project/exp2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable tdd_sample_test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tdd_sample_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/tdd_sample_test.dir/build: tdd_sample_test
.PHONY : CMakeFiles/tdd_sample_test.dir/build

CMakeFiles/tdd_sample_test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tdd_sample_test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tdd_sample_test.dir/clean

CMakeFiles/tdd_sample_test.dir/depend:
	cd /home/taki/CATdd/target_project/exp2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/taki/CATdd/target_project/exp2 /home/taki/CATdd/target_project/exp2 /home/taki/CATdd/target_project/exp2/build /home/taki/CATdd/target_project/exp2/build /home/taki/CATdd/target_project/exp2/build/CMakeFiles/tdd_sample_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/tdd_sample_test.dir/depend

