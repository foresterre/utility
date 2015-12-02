@echo off

REM Enter out
pushd out

REM Enter exe
pushd exe
del /Q /S *.*
popd
REM Left exe

REM Enter im
pushd im
del /Q /S *.*
popd
REM Left im

popd
REM Left out
