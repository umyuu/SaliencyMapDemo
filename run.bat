@echo on

cd %~dp0
call .venv\Scripts\activate
uv run --verbose Python app.py --server_port 9999

TIMEOUT /T 10
