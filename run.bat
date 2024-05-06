@echo on

cd %~dp0
call venv\Scripts\activate
python src\launch.py --server_port 9999

TIMEOUT /T 10