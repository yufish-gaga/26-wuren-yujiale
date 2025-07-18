cmake_minimum_required(VERSION 3.10)

project(TEST)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(
    ${PROJECT_SOURCE_DIR}/CMake1/common/kalman/include
    ${PROJECT_SOURCE_DIR}/CMake1/common/math/include
    ${PROJECT_SOURCE_DIR}/CMake1/modules/A1/include
    ${PROJECT_SOURCE_DIR}/CMake1/modules/A2/include
    ${PROJECT_SOURCE_DIR}/CMake1/modules/M1/include
    ${PROJECT_SOURCE_DIR}/CMake1/modules/M2/include
)

find_package(OpenCV REQUIRED)

add_subdirectory(CMake1/common)
add_subdirectory(CMake1/modules)

add_executable(test CMake1/main.cpp CMake1/modules/M2/src/M2.cpp CMake1/modules/M1/src/M1.cpp CMake1/modules/A2/src/A2.cpp CMake1/modules/A1/src/A11.cpp CMake1/modules/A1/src/A12.cpp CMake1/modules/A1/src/A13.cpp CMake1/common/math/src/Math.cpp)

target_link_libraries(test
    PRIVATE
    M1
    A1
    ${OpenCV_LIBS}
)

