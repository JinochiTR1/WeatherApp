@echo off
REM kontrola virtuálního prostředí
IF NOT EXIST venv (
    echo Vytvarim virtualni prostredi...
    python -m venv venv
)

REM aktivace venv
call venv\Scripts\activate

REM kontrola a instalace baliku flask
pip show flask >nul 2>&1
IF ERRORLEVEL 1 (
    echo Instalace Flask...
    pip install flask
)

REM kontrola a instalace baliku requests
pip show requests >nul 2>&1
IF ERRORLEVEL 1 (
    echo Instalace Requests...
    pip install requests
)

REM spusteni hlavniho skriptu
echo Spoustim pocasi.py
python pocasi.py
