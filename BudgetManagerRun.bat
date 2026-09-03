@echo off
set "FOLDER=C:\BudgetManager"
cd /d "%FOLDER%"

:LOOP
cls
echo Opening DailyUpdate.txt...
start /wait "" "DailyUpdate.txt"

echo Processing budget...
python "BudgetManagerScript.py"

REM
if %ERRORLEVEL% EQU 10 (
    goto LOOP
)

pause