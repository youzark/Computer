# simple test without complex lib structure
cmake_minimum_required(VERSION 3.16.3)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(iterator)

add_executable(iterator src/main.cpp src/printer.cpp)

target_include_directories(Tester PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# install(TARGET Tester DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bin)

