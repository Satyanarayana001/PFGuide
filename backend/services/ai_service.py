from collections.abc import Mapping
from typing import Any


def build_claim_explanation(application: Mapping[str, Any]) -> dict[str, Any]:
    """Create deterministic, citizen-friendly guidance for a synthetic claim."""
    status = str(application.get("status", "")).upper()
    application_id = str(application.get("application_id", ""))
    issue = str(application.get("issue", "the recorded claim issue")).rstrip(".")
    next_action = str(application.get("next_action", "Review the synthetic claim status."))

    if status == "ACTION_REQUIRED":
        explanation = {
            "what_happened": (
                f"Your claim cannot move forward yet because {issue.lower()}."
            ),
            "why": (
                "The required verification must be completed during this stage before "
                "the claim can continue for further processing."
            ),
            "what_now": [
                next_action,
                "Ask the appropriate team to complete the pending verification.",
                "Check your synthetic claim status again after the verification is completed.",
            ],
        }
    elif status == "PROCESSING":
        explanation = {
            "what_happened": "Your claim is still moving through the synthetic processing workflow.",
            "why": (
                "The claim has been received and is being reviewed at the current "
                "processing stage."
            ),
            "what_now": [
                "Allow time for the current processing stage to finish.",
                next_action,
                "Check the synthetic claim status again for an update.",
            ],
        }
    elif status == "APPROVED":
        explanation = {
            "what_happened": "Your synthetic claim has been approved.",
            "why": "The claim completed the required review steps in this prototype workflow.",
            "what_now": [
                "Expect the approved claim to move to the next simulated completion step.",
                "Keep the application reference available for future status checks.",
                next_action,
            ],
        }
    else:
        explanation = {
            "what_happened": "This synthetic claim has an unrecognised status.",
            "why": "The prototype does not have guidance for this status yet.",
            "what_now": [next_action],
        }

    return {
        "application_id": application_id,
        "status": status,
        "demo": True,
        **explanation,
    }
