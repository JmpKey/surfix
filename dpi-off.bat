@echo off

:loop
REM Change to your anti-DPI solution
start "" "C:\your\path\anti-dpi.exe" -param1 -param2

REM Change to your program
start "" "C:\your\path\program.exe" -param1 -param2

:wait
REM your anti-DPI solution
tasklist | find /i "anti-dpi.exe" >nul
if errorlevel 1 (
	REM your program
    taskkill /IM "program.exe" /F
    exit /b
)

REM your program
tasklist | find /i "program.exe" >nul
if errorlevel 1 (
	REM your anti-DPI solution
    taskkill /IM "anti-dpi.exe" /F
    exit /b
)

timeout /t 5 >nul
goto wait
