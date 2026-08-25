import json
from typing import Any

try:
    from core.config import MOCK_DATA_DIR
except ModuleNotFoundError:
    from backend.core.config import MOCK_DATA_DIR


def get_application(application_id: str) -> dict[str, Any] | None:
    """Return a synthetic application by ID, or None when it cannot be found."""
    try:
        with (MOCK_DATA_DIR / "applications.json").open(encoding="utf-8") as data_file:
            payload = json.load(data_file)
    except (OSError, json.JSONDecodeError):
        return None

    applications = payload.get("applications") if isinstance(payload, dict) else None
    if not isinstance(applications, list):
        return None

    return next(
        (
            application
            for application in applications
            if isinstance(application, dict)
            and application.get("application_id") == application_id
        ),
        None,
    )
