@echo on

cd %~dp0
call venv\Scripts\activate
gradio app.py

TIMEOUT /T 10
