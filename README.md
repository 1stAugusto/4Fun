# DevOps Pipeline Lab

[![CI](https://github.com/1stAugusto/4Fun/actions/workflows/ci.yml/badge.svg)](https://github.com/1stAugusto/4Fun/actions/workflows/ci.yml)

A small FastAPI service used to practice a container-based delivery pipeline, from local development and automated checks to a public deployment.

## Live demo

- **API:** https://devops-pipeline-lab.onrender.com
- **Interactive API docs:** https://devops-pipeline-lab.onrender.com/docs
- **Health check:** https://devops-pipeline-lab.onrender.com/health
- **Runtime information:** https://devops-pipeline-lab.onrender.com/info

The API currently provides `/health` and `/info`. The root path (`/`) is not defined, so it returns `404 Not Found` by design.

## Technology and pipeline

- Python and FastAPI
- Docker image built from `Dockerfile`; the application runs as a non-root user
- Docker Compose for local container orchestration
- GitHub Actions runs the tests, builds and starts the container, checks both endpoints and verifies the container does not run as root
- On pushes to `main`, GitHub Actions publishes the image to GitHub Container Registry (GHCR)
- Render builds from the GitHub repository and automatically deploys commits from `main`

## Run locally

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the API:

```powershell
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the API, or visit `/health` and `/info` on that address.

### Configuration

`APP_VERSION` and `APP_ENV` configure the information returned by `/info`. Locally, they default to `0.1.0` and `development`.

```powershell
$env:APP_VERSION = "0.2.0"
$env:APP_ENV = "staging"
python -m uvicorn app.main:app --reload
```

## Run tests

```powershell
python -m pytest -q
```

## Run with Docker Compose

Build the image and start the API in the background:

```powershell
docker compose up --build --detach
```

Check the container status and open `http://127.0.0.1:8000/health` or `http://127.0.0.1:8000/info`:

```powershell
docker compose ps
```

Stop the service and remove its container and network:

```powershell
docker compose down
```

Compose defaults to `APP_VERSION=0.1.0` and `APP_ENV=development`. You can override these in the PowerShell session before starting Compose:

```powershell
$env:APP_VERSION = "0.2.0"
$env:APP_ENV = "staging"
docker compose up --build --detach
```

## Deployment notes

The container listens on the port supplied by `PORT`, falling back to `8000` for local Docker use. Render supplies `PORT` for web services; the service binds to `0.0.0.0` and uses `/health` as its health check. The Render free instance may sleep after inactivity and take about a minute to respond to the next request.

## Repository

Source code: https://github.com/1stAugusto/4Fun
