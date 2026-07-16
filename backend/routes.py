from fastapi import APIRouter

from services import health_check
from schemas import ApiResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=ApiResponse
)
async def health() -> ApiResponse:
    return await health_check()