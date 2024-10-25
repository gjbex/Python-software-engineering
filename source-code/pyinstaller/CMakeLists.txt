cmake_minimum_required(VERSION 3.20)

project(pyinstaller)

# ensure a Python 3 interpreter and development libraries are available
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# create a custom command to build the executables
add_custom_command(
    OUTPUT dist/prod_columns dist/sum_columns
    COMMAND python -m venv ${CMAKE_CURRENT_BINARY_DIR}/build_venv
    COMMAND ${CMAKE_CURRENT_BINARY_DIR}/build_venv/bin/pip install
                -r ${CMAKE_CURRENT_SOURCE_DIR}/requirements.txt
    COMMAND ${CMAKE_CURRENT_BINARY_DIR}/build_venv/bin/pyinstaller --onefile
                --hidden-import funcs --collect-submodules funcs
                ${CMAKE_CURRENT_SOURCE_DIR}/src/sum_columns.py
    COMMAND ${CMAKE_CURRENT_BINARY_DIR}/build_venv/bin/pyinstaller --onefile
                --add-data ${CMAKE_CURRENT_SOURCE_DIR}/data.csv:.
                --hidden-import funcs --collect-submodules funcs
                ${CMAKE_CURRENT_SOURCE_DIR}/src/prod_columns.py
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/src/prod_columns.py
            ${CMAKE_CURRENT_SOURCE_DIR}/src/sum_columns.py
            ${CMAKE_CURRENT_SOURCE_DIR}/src/lib/funcs.py
            ${CMAKE_CURRENT_SOURCE_DIR}/data.csv
    VERBATIM)

# create a custom target to build the executables
add_custom_target(create_executables ALL
    DEPENDS dist/prod_columns dist/sum_columns)

# install the executables
install(
    FILES ${CMAKE_BINARY_DIR}/dist/prod_columns ${CMAKE_BINARY_DIR}/dist/sum_columns
    DESTINATION bin
)
