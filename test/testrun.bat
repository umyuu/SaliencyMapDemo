@echo on

cd %~dp0
call ..\venv\Scripts\activate
python -m unittest -v test_create_grayscale_gradation.py

TIMEOUT /T 30