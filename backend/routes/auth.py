from fastapi import APIRouter, HTTPException, status

try:
    from models.schemas import DemoLoginResponse
    from services.auth_service import get_demo_user
except ModuleNotFoundError:
    from backend.models.schemas import DemoLoginResponse
    from backend.services.auth_service import get_demo_user

router = APIRouter(prefix="/api/auth", tags=["authentication"])


@router.post("/demo-login", response_model=DemoLoginResponse)
def demo_login() -> DemoLoginResponse:
    user = get_demo_user()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Synthetic demo user data is unavailable.",
        )

    try:
        return DemoLoginResponse(
            demo=True,
            user_id=user["user_id"],
            display_name=user["display_name"],
            application_id=user["application_id"],
            message="Demo access granted. All data is synthetic.",
        )
    except (KeyError, TypeError) as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Synthetic demo user data is invalid.",
        ) from error
