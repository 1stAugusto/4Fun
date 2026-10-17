from fastapi import FastAPI

app = FastAPI(title="DevOps Pipeline Lab")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return a simple status used by operators and deployment checks."""
    return {"status": "ok"}
