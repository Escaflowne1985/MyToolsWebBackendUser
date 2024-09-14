@echo off
setlocal

set PORT=9000

:: 查找占用端口的进程ID
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%PORT%') do (
    set PID=%%a
)

:: 检查是否找到了PID
if "%PID%"=="" (
    echo No process found using port %PORT%.
    goto :EOF
)

:: 杀掉进程
echo Killing process with PID %PID%...
taskkill /PID %PID% /F
echo Process terminated.
endlocal
