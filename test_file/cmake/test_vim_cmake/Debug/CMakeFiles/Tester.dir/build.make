# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/hyx/Computer/test_file/cmake/test_vim_cmake

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug

# Include any dependencies generated for this target.
include CMakeFiles/Tester.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Tester.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Tester.dir/flags.make

CMakeFiles/Tester.dir/src/main.cpp.o: CMakeFiles/Tester.dir/flags.make
CMakeFiles/Tester.dir/src/main.cpp.o: ../src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Tester.dir/src/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Tester.dir/src/main.cpp.o -c /home/hyx/Computer/test_file/cmake/test_vim_cmake/src/main.cpp

CMakeFiles/Tester.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Tester.dir/src/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/hyx/Computer/test_file/cmake/test_vim_cmake/src/main.cpp > CMakeFiles/Tester.dir/src/main.cpp.i

CMakeFiles/Tester.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Tester.dir/src/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/hyx/Computer/test_file/cmake/test_vim_cmake/src/main.cpp -o CMakeFiles/Tester.dir/src/main.cpp.s

CMakeFiles/Tester.dir/src/printer.cpp.o: CMakeFiles/Tester.dir/flags.make
CMakeFiles/Tester.dir/src/printer.cpp.o: ../src/printer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Tester.dir/src/printer.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Tester.dir/src/printer.cpp.o -c /home/hyx/Computer/test_file/cmake/test_vim_cmake/src/printer.cpp

CMakeFiles/Tester.dir/src/printer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Tester.dir/src/printer.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/hyx/Computer/test_file/cmake/test_vim_cmake/src/printer.cpp > CMakeFiles/Tester.dir/src/printer.cpp.i

CMakeFiles/Tester.dir/src/printer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Tester.dir/src/printer.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/hyx/Computer/test_file/cmake/test_vim_cmake/src/printer.cpp -o CMakeFiles/Tester.dir/src/printer.cpp.s

# Object files for target Tester
Tester_OBJECTS = \
"CMakeFiles/Tester.dir/src/main.cpp.o" \
"CMakeFiles/Tester.dir/src/printer.cpp.o"

# External object files for target Tester
Tester_EXTERNAL_OBJECTS =

Tester: CMakeFiles/Tester.dir/src/main.cpp.o
Tester: CMakeFiles/Tester.dir/src/printer.cpp.o
Tester: CMakeFiles/Tester.dir/build.make
Tester: CMakeFiles/Tester.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable Tester"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Tester.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Tester.dir/build: Tester

.PHONY : CMakeFiles/Tester.dir/build

CMakeFiles/Tester.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Tester.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Tester.dir/clean

CMakeFiles/Tester.dir/depend:
	cd /home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/hyx/Computer/test_file/cmake/test_vim_cmake /home/hyx/Computer/test_file/cmake/test_vim_cmake /home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug /home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug /home/hyx/Computer/test_file/cmake/test_vim_cmake/Debug/CMakeFiles/Tester.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Tester.dir/depend

