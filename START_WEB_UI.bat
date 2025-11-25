@echo off
echo Starting AI Teaching Assistant Web UI (Ollama Version)...
echo.
echo Open your browser to: http://localhost:5000
echo.
cd /d "%~dp0"
python app_ollama.py
pause
