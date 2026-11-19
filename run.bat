@echo off
title Momentrix - Turn Hours into Moments
echo ========================================================
echo   MOMENTRIX - Turn Hours into Moments.
echo   Autonomous AI Video Clipping Platform
echo ========================================================

REM Automatically launch browser to the Momentrix landing page
start http://127.0.0.1:8765

REM Use the installed Python 3.11 with all ML and clipping packages
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    echo Using Python 3.11 with all packages installed...
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" -m studio.server
    goto end
)

if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe" (
    "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe" -m studio.server
    goto end
)

python -m studio.server

:end
pause
