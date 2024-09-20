@echo off
setlocal enabledelayedexpansion

set PORT=9000

:: 初始化PID为空
set PID=

:: 查找占用端口的进程ID
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%PORT%') do (
    set PID=%%a
    goto :FOUND_PID
)

:: 如果没有找到PID
echo No process found using port %PORT%.
goto :EOF

:FOUND_PID
:: 检查是否找到PID
if defined PID (
    echo Killing process with PID !PID!...
    taskkill /PID !PID! /F
    echo Process terminated.
) else (
    echo No process found using port %PORT%.
)

endlocal
