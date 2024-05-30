@echo on

cd %~dp0
cd ..
call venv\Scripts\activate
gradio app.py

TIMEOUT /T 10
