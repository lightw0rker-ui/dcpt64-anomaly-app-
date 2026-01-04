# Windows PowerShell install script - creates .venv and installs requirements
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
& .\.venv\Scripts\python.exe -m pip install -r backend/requirements-dev.txt
