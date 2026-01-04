.PHONY: venv install run test

venv:
	python -m venv .venv

install: venv
	python -m pip install --upgrade pip
	python -m pip install -r backend/requirements.txt
	python -m pip install -r backend/requirements-dev.txt

run:
	uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

test:
	pytest -q
