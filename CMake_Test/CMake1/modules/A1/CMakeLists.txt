# A1/CMakeLists.txt
add_library(A1 
    src/A11.cpp  
    src/A12.cpp
    src/A13.cpp
)

# A1的头文件路径（让M1模块引用）
target_include_directories(A1
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)