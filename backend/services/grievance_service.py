import json
import os
import secrets
import tempfile
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from core.config import MOCK_DATA_DIR
    from services.ai_service import build_claim_explanation
    from services.application_service import get_application
except ModuleNotFoundError:
    from backend.core.config import MOCK_DATA_DIR
    from backend.services.ai_service import build_claim_explanation
    from backend.services.application_service import get_application

GRIEVANCES_PATH = MOCK_DATA_DIR / "grievances.json"


class GrievanceStorageError(Exception):
    """Raised when simulated grievance storage cannot be safely used."""


def get_grievance_draft(application_id: str) -> dict[str, Any] | None:
    """Create a professional draft for a known synthetic application."""
    application = get_application(application_id.strip())
    if application is None:
        return None

    explanation = build_claim_explanation(application)
    claim_type = str(application.get("claim_type", "PF claim"))
    stage = str(application.get("current_stage", "current review"))
    issue = str(application.get("issue", "the recorded claim issue")).rstrip(".")
    next_action = str(application.get("next_action", "Review the synthetic claim status."))
    subject = f"Assistance needed with {issue.lower()}"

    return {
        "application_id": str(application["application_id"]),
        "subject": subject,
        "message": (
            f"My synthetic {claim_type} is currently at the {stage} stage. "
            f"The current issue shown is that {issue.lower()}. "
            "I would like assistance in understanding what is required to move "
            f"my claim forward. The suggested next step is: {next_action}"
        ),
        "demo": bool(explanation["demo"]),
    }


def submit_grievance(
    application_id: str, subject: str, message: str
) -> dict[str, Any] | None:
    """Store a simulated grievance for a known application and return its receipt."""
    application = get_application(application_id.strip())
    if application is None:
        return None

    grievances = _load_grievances()
    reference_number = _generate_reference_number(grievances)
    grievance = {
        "reference_number": reference_number,
        "application_id": str(application["application_id"]),
        "subject": subject,
        "message": message,
        "status": "SUBMITTED",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "demo": True,
    }
    grievances.append(grievance)
    _write_grievances(grievances)

    return {
        "reference_number": reference_number,
        "application_id": grievance["application_id"],
        "status": "SUBMITTED",
        "message": "Your demo grievance has been submitted successfully.",
        "demo": True,
    }


def _load_grievances() -> list[dict[str, Any]]:
    try:
        with GRIEVANCES_PATH.open(encoding="utf-8") as data_file:
            payload = json.load(data_file)
    except (OSError, json.JSONDecodeError) as error:
        raise GrievanceStorageError("Mock grievance storage is unavailable.") from error

    grievances = payload.get("grievances") if isinstance(payload, dict) else None
    if not isinstance(grievances, list) or not all(
        isinstance(grievance, dict) for grievance in grievances
    ):
        raise GrievanceStorageError("Mock grievance storage is invalid.")

    return grievances


def _generate_reference_number(grievances: list[dict[str, Any]]) -> str:
    existing_references = {
        str(grievance.get("reference_number", "")) for grievance in grievances
    }
    for _ in range(10):
        reference_number = f"GRV-2026-{secrets.randbelow(1_000_000):06d}"
        if reference_number not in existing_references:
            return reference_number

    raise GrievanceStorageError("Could not generate a unique demo grievance reference.")


def _write_grievances(grievances: list[dict[str, Any]]) -> None:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=GRIEVANCES_PATH.parent,
            prefix="grievances-",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
            json.dump({"grievances": grievances}, temporary_file, indent=2)
            temporary_file.write("\n")
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
        os.replace(temporary_path, GRIEVANCES_PATH)
    except OSError as error:
        raise GrievanceStorageError("Mock grievance storage is unavailable.") from error
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink(missing_ok=True)
