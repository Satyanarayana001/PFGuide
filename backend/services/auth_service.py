import json
from typing import Any

try:
    from core.config import MOCK_DATA_DIR
except ModuleNotFoundError:
    from backend.core.config import MOCK_DATA_DIR


def get_demo_user() -> dict[str, Any] | None:
    """Return the single synthetic demo user, or None when data is unavailable."""
    try:
        with (MOCK_DATA_DIR / "users.json").open(encoding="utf-8") as data_file:
            payload = json.load(data_file)
    except (OSError, json.JSONDecodeError):
        return None

    users = payload.get("users") if isinstance(payload, dict) else None
    if not isinstance(users, list) or not users or not isinstance(users[0], dict):
        return None

    return users[0]
