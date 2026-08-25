from fastapi import APIRouter, HTTPException, status

try:
    from models.schemas import ApplicationResponse, ClaimExplanationResponse
    from services.ai_service import build_claim_explanation
    from services.application_service import get_application
except ModuleNotFoundError:
    from backend.models.schemas import ApplicationResponse, ClaimExplanationResponse
    from backend.services.ai_service import build_claim_explanation
    from backend.services.application_service import get_application

router = APIRouter(prefix="/api/applications", tags=["applications"])


@router.get("/{application_id}/explanation", response_model=ClaimExplanationResponse)
def read_application_explanation(application_id: str) -> ClaimExplanationResponse:
    application = get_application(application_id.strip())
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )

    try:
        return ClaimExplanationResponse.model_validate(build_claim_explanation(application))
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Synthetic application data is invalid.",
        ) from error


@router.get("/{application_id}", response_model=ApplicationResponse)
def read_application(application_id: str) -> ApplicationResponse:
    application = get_application(application_id.strip())
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )

    try:
        return ApplicationResponse.model_validate(application)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Synthetic application data is invalid.",
        ) from error
