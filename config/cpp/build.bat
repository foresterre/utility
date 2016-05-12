@echo off

REM Do not add spaces next to the variable name and its value!
REM Otherwise it will break the set command

set fname=main
set cpp_ext=.cc
set obj_ext=.o
set bin_ext=.exe

set include_path=
set lib_path=


REM Additional compile and link arguments can be defined below
set add_compile_args=-Wall -std=c++14
set add_link_args=

REM Arguments (if provided) for the binary executable
set bin_run_args=

g++ -c src/%fname%%cpp_ext% -o out/im/%fname%%obj_ext% -I%include_path% %add_compile_args% && ^
g++ out/im/%fname%%obj_ext% -o out/exe/%fname%%bin_ext% -L%lib_path% %add_link_args%

pushd out
pushd exe
REM Execute executable with defined arguments (if any).
"%fname%%bin_ext%" %bin_run_args%
popd
popd