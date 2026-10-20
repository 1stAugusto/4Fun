import os

from fastapi import FastAPI

app = FastAPI(title="DevOps Pipeline Lab")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a simple status used by operators and deployment checks."""
    return {"status": "ok"}


@app.get("/info")
def app_info() -> dict[str, str]:
    """Expose non-sensitive build and runtime information."""
    return {
        "service": app.title,
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "development"),
    }
