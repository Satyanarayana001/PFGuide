from fastapi import APIRouter

try:
    from models.schemas import HealthResponse
except ModuleNotFoundError:
    from backend.models.schemas import HealthResponse

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="PFGuide API")
