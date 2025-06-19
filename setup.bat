@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

echo Vítej v aplikaci pro Počasí!
echo Pro pokračování do aplikace bude potřeba vytvořit virtuální prostředí a nainstalovat balíček: requests.
set /p ANS= Přejete si pokračovat? [A/N]:
if /I not "%ANS%"=="A" exit /b

if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate

pip install requests

python pocasi.py
