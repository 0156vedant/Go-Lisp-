@echo off
echo Compiling wisp2.cpp...
g++ wisp2.cpp -o wisp_interpreter
if %errorlevel% neq 0 (
    echo Compilation failed. Exiting...
    exit /b 1
)

echo Starting FastAPI server...
start cmd /c "uvicorn server:app --host 127.0.0.1 --port 5001"
echo Server started at http://127.0.0.1:5001
pause
