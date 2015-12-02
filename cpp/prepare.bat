@echo off
echo -------------------
echo Before prepare.bat:
echo -------------------
call dir /D /S

REM local root
REM - src
REM - out
mkdir src
mkdir out

REM Enter out
pushd out

REM local root
REM - src
REM - out
REM   - im
REM   - exe
mkdir im
mkdir exe

popd
REM Leave out

echo ------------------
echo After prepare.bat:
echo ------------------
call dir /D /S