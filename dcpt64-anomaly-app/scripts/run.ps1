# Windows PowerShell run script - runs the dev server using the venv python
& .\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
