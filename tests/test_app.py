import os

from app.app import app


def test_health_check(monkeypatch):
    os.environ["APP_ENV"] = "development"

    monkeypatch.setattr("app.app.check_database", lambda: True)

    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["service"] == "devops-learning"
    assert response.json["environment"] == "development"
    assert response.json["database"] == "connected"
