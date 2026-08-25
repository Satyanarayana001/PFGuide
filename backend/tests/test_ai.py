from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_action_required_explanation_returns_guidance() -> None:
    response = client.get("/api/applications/APP-2026-1001/explanation")

    assert response.status_code == 200
    payload = response.json()
    assert payload["application_id"] == "APP-2026-1001"
    assert payload["status"] == "ACTION_REQUIRED"
    assert payload["demo"] is True
    assert payload["what_happened"]
    assert payload["why"]
    assert isinstance(payload["what_now"], list)
    assert payload["what_now"]


def test_processing_explanation_returns_guidance() -> None:
    response = client.get("/api/applications/APP-2026-1002/explanation")

    assert response.status_code == 200
    assert response.json()["status"] == "PROCESSING"


def test_unknown_application_explanation_returns_not_found() -> None:
    response = client.get("/api/applications/APP-UNKNOWN/explanation")

    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found."}
