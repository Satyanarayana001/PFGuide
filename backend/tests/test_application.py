from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_primary_application_returns_expected_fields() -> None:
    response = client.get("/api/applications/APP-2026-1001")

    assert response.status_code == 200
    payload = response.json()
    for field in ("status", "current_stage", "issue", "next_action"):
        assert field in payload


def test_unknown_application_returns_not_found() -> None:
    response = client.get("/api/applications/APP-UNKNOWN")

    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found."}
