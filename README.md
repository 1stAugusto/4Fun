# DevOps Pipeline Lab

Small Python API project for practicing a delivery pipeline.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the API

```powershell
uvicorn app.main:app --reload --host 0.0.0.0
```

Open `http://127.0.0.1:8000/health` to check the health endpoint, or
`http://127.0.0.1:8000/info` to inspect the service version and runtime
environment. Visit `http://127.0.0.1:8000/docs` for the interactive API docs.

The `/info` endpoint reads `APP_VERSION` and `APP_ENV` from environment
variables. Locally, they default to `0.1.0` and `development`; the Docker image
sets them to `0.1.0` and `container`. They can be overridden at runtime.

## Run tests

```powershell
pytest -q
```
