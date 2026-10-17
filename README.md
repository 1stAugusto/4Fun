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

Open `http://127.0.0.1:8000/health` to check the health endpoint, or visit
`http://127.0.0.1:8000/docs` for the interactive API documentation.

## Run tests

```powershell
pytest -q
```
