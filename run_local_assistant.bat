@echo off
setlocal enabledelayedexpansion

echo ============================================================
echo AI TEACHING ASSISTANT - LOCAL SETUP & RUN
echo ============================================================
echo.

REM --- Step 1: Find Ollama ---
echo [1/5] Searching for Ollama...
set "OLLAMA_EXE="

REM Check PATH
where ollama >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set "OLLAMA_EXE=ollama"
    echo Found Ollama in PATH.
) else (
    REM Check common locations
    if exist "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" (
        set "OLLAMA_EXE=%LOCALAPPDATA%\Programs\Ollama\ollama.exe"
        echo Found Ollama in Local AppData.
    ) else if exist "C:\Program Files\Ollama\ollama.exe" (
        set "OLLAMA_EXE=C:\Program Files\Ollama\ollama.exe"
        echo Found Ollama in Program Files.
    )
)

if "%OLLAMA_EXE%"=="" (
    echo.
    echo [ERROR] Ollama not found!
    echo Please download and install Ollama from: https://ollama.ai/download
    echo After installing, run this script again.
    echo.
    pause
    exit /b 1
)

REM --- Step 2: Check/Start Server ---
echo.
echo [2/5] Checking Ollama Server...
tasklist /FI "IMAGENAME eq ollama_app.exe" 2>NUL | find /I /N "ollama_app.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo Ollama app is running.
) else (
    echo Starting Ollama server...
    start "Ollama Server" "%OLLAMA_EXE%" serve
    echo Waiting for server to start...
    timeout /t 5 /nobreak >nul
)

REM --- Step 3: Pull Models ---
echo.
echo [3/5] Checking/Pulling Models (this may take a while)...
echo Pulling 'mistral' (LLM)...
"%OLLAMA_EXE%" pull mistral
echo Pulling 'nomic-embed-text' (Embeddings)...
"%OLLAMA_EXE%" pull nomic-embed-text

REM --- Step 4: Install Python Deps ---
echo.
echo [4/5] Installing Python Dependencies...
pip install -r requirements.txt
pip install langchain-community sentence-transformers chromadb

REM --- Step 5: Run Assistant ---
echo.
echo [5/5] Starting AI Teaching Assistant...
echo.
python main_ollama.py

pause
