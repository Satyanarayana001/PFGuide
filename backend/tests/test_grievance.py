import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)
GRIEVANCES_PATH = Path(__file__).resolve().parents[1] / "mock_data" / "grievances.json"


@pytest.fixture(autouse=True)
def restore_grievance_data() -> None:
    """Keep the repository's simulated grievance store unchanged after each test."""
    original_data = GRIEVANCES_PATH.read_bytes()
    try:
        yield
    finally:
        GRIEVANCES_PATH.write_bytes(original_data)


def test_grievance_draft_is_generated_for_known_application() -> None:
    response = client.post("/api/applications/APP-2026-1001/grievance/draft")

    assert response.status_code == 200
    payload = response.json()
    assert payload["subject"]
    assert payload["message"]
    assert payload["demo"] is True


def test_unknown_application_grievance_draft_returns_not_found() -> None:
    response = client.post("/api/applications/APP-UNKNOWN/grievance/draft")

    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found."}


def test_grievance_submission_returns_and_stores_synthetic_reference() -> None:
    response = client.post(
        "/api/grievances",
        json={
            "application_id": "APP-2026-1001",
            "subject": "Help with synthetic verification",
            "message": "Please help me understand the required verification step.",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["reference_number"].startswith("GRV-2026-")
    assert payload["status"] == "SUBMITTED"
    assert payload["demo"] is True

    stored_grievances = json.loads(GRIEVANCES_PATH.read_text(encoding="utf-8"))["grievances"]
    assert any(
        grievance["reference_number"] == payload["reference_number"]
        for grievance in stored_grievances
    )


def test_grievance_submission_for_unknown_application_returns_not_found() -> None:
    response = client.post(
        "/api/grievances",
        json={
            "application_id": "APP-UNKNOWN",
            "subject": "Help requested",
            "message": "This is a synthetic request.",
        },
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found."}
