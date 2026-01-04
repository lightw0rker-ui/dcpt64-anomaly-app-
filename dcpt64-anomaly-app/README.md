DCPT-64 Anomaly MVP

Quick start (POSIX / macOS / WSL / Git Bash):

- Create venv and install:

  make install

- Run server (dev):

  make run

- Run tests:

  make test

Windows (PowerShell):

- Install:

  .\scripts\install.ps1

- Run:

  .\scripts\run.ps1

Notes:
- Requirements files are in `backend/requirements.txt` and `backend/requirements-dev.txt`.
- The server will create cache files under `backend/app/cache/` on first run.
