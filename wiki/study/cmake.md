## Article 1: Cmake basics 
https://www.siliceum.com/en/blog/post/cmake_01_cmake-basics
structure:
* why cmake
* the cmake_list file:
	* basic
	* target
	* more control
* sturcture of cmakefile

estimate time: 30 mins
	
* Summary :
'''
myawesomeproject
├── CMakeLists.txt
└── libs
    ├── CMakeLists.txt
    ├── libA
    │   ├── CMakeLists.txt
    │   └── include
    │       └── libA.h
    ├── libB
    │   ├── CMakeLists.txt
    │   ├── include
    │   │   └── libB.h
    │   └── src
    │       └── libB.cpp
    └── programA
        ├── CMakeLists.txt
        └── src
            └── main.cpp
./CMakeLists.txt

cmake_minimum_required(VERSION 3.14)
project(myawesomeproject VERSION 1.0 LANGUAGES C CXX) # CXX stands for c++
add_subdirectory(libs)

libs/CMakeLists.txt

add_subdirectory(libA)
add_subdirectory(libB)
add_subdirectory(programA)

libs/libA/CMakeLists.txt

add_library(libA INTERFACE)   
target_include_directories(libA INTERFACE include/)


libs/libB/CMakeLists.txt
add_library(libB src/lib.cpp include/labB.h)
target_include_directories(libB PUBLIC include/)
target_link_libraries(libB PRIVATE libA) # libA is only exposed to libB

libs/programA/CMakeLists.txt
add_executable(programA src/main.cpp)
target_link_libraries(programA PRIVATE libB)  #libA is only exposed to libB is only exposed to programA

'''
## Article 2:Cmake by example:
summary:
install(TARGETS myapp DESTINATION bin) this will install target myapp to bin/

cmake .. -DCMAKE_INSTALL_PREFIX=../_install 
	this will tell cmake install executable to ../_install rather than system 


## Aritcle 3:about library installation and package and version control
https://www.foonathan.net/2016/03/cmake-install/

''''''

file directory:
 include/
   my_library/
     headera.hpp
	 headerb.hpp
	 config.hpp
	 ...
 src/
   source-a.cpp
   source-b.cpp
   config.hpp.in
   ...
   CMakeLists.txt
 example/
   example-a.cpp
   ...
   CMakeLists.txt
 tool/
   tool.cpp
   CMakeLists.txt
 test/
   test.cpp
   CMakeLists.txt
 CMakeLists.txt
 ...


''''''

1. set variables:
set(MY_LIBRARY_VERSION_MAJOR 1 CACHE STRING "major version" FORCE)
set(MY_LIBRARY_VERSION_MINOR 0 CACHE STRING "minor version" FORCE)
set(MY_LIBRARY_VERSION ${MY_LIBRARY_VERSION_MAJOR}.${MY_LIBRARY_VERSION_MINOR} CACHE STRING "version" FORCE)

specification:
set(<variable> <value>
    [[CACHE <type> <docstring> [FORCE]] | PARENT_SCOPE])

2. set options (provide options)
option(<variable> "<help_text>" [value])

option(MY_LIBRARY_USE_FANCY_NEW_CLASS "whether or not to use fancy new class" ON)
option(MY_LIBRARY_DEBUG_MODE "whether or not debug mode is activated" OFF)

3. a good practice
set(header_path "${MY_LIBRARY_SOURCE_DIR}/include/my_library")
set(header ${header_path}/header-a.hpp
		   ${header_path}/header-b.hpp
		   ${header_path}/config.hpp
		   ...)

set source files
set(src source-a.cpp
		source-b.cpp
		...)
		
configure config.hpp.in
configure_file("config.hpp.in" "${CMAKE_CURRENT_BINARY_DIR}/config_impl.hpp")

define library target
add_library(my_library ${header} ${src})
target_include_directories(my_library PUBLIC ${MY_LIBRARY_SOURCE_DIR}/include
											 ${CMAKE_CURRENT_BINARY_DIR})


Summary:
this artical talks about how to make a library through and how to make it
publishable.
it contains not only build system but also :
exporting
packaging
version control
out of my scope
