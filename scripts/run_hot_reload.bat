REM Gradioのオートリロード用のスクリプトです。
@echo on

cd %~dp0
cd ..
call .venv\Scripts\activate
uv run gradio app.py

TIMEOUT /T 10
