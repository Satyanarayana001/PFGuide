from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_demo_login_returns_synthetic_user() -> None:
    response = client.post("/api/auth/demo-login")

    assert response.status_code == 200
    payload = response.json()
    assert payload["demo"] is True
    assert payload["application_id"] == "APP-2026-1001"
    assert payload["message"] == "Demo access granted. All data is synthetic."
