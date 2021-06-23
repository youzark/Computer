
cmake_minimum_required(VERSION 3.16.3)

project(PSRS)

find_package(MPI)
include_directories(SYSTEM ${MPI_INCLUDE_PATH})

add_compile_options()

add_executable(${PROJECT_NAME} psrs.c)

target_link_libraries(${PROJECT_NAME} ${MPI_C_LIBRARIES})
