from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_ok() -> None:
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_info_returns_runtime_configuration(monkeypatch) -> None:
    monkeypatch.setenv("APP_VERSION", "test-version")
    monkeypatch.setenv("APP_ENV", "test")

    with TestClient(app) as client:
        response = client.get("/info")

    assert response.status_code == 200
    assert response.json() == {
        "service": "DevOps Pipeline Lab",
        "version": "test-version",
        "environment": "test",
    }
