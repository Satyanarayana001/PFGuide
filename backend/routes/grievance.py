from fastapi import APIRouter, HTTPException, status

try:
    from models.schemas import (
        GrievanceDraftResponse,
        GrievanceSubmissionResponse,
        GrievanceSubmitRequest,
    )
    from services.grievance_service import (
        GrievanceStorageError,
        get_grievance_draft,
        submit_grievance,
    )
except ModuleNotFoundError:
    from backend.models.schemas import (
        GrievanceDraftResponse,
        GrievanceSubmissionResponse,
        GrievanceSubmitRequest,
    )
    from backend.services.grievance_service import (
        GrievanceStorageError,
        get_grievance_draft,
        submit_grievance,
    )

router = APIRouter(tags=["grievances"])


@router.post(
    "/api/applications/{application_id}/grievance/draft",
    response_model=GrievanceDraftResponse,
)
def create_grievance_draft(application_id: str) -> GrievanceDraftResponse:
    draft = get_grievance_draft(application_id)
    if draft is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )
    return GrievanceDraftResponse.model_validate(draft)


@router.post("/api/grievances", response_model=GrievanceSubmissionResponse)
def create_grievance_submission(
    grievance: GrievanceSubmitRequest,
) -> GrievanceSubmissionResponse:
    try:
        receipt = submit_grievance(
            grievance.application_id, grievance.subject, grievance.message
        )
    except GrievanceStorageError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Mock grievance storage is unavailable.",
        ) from error

    if receipt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )
    return GrievanceSubmissionResponse.model_validate(receipt)
