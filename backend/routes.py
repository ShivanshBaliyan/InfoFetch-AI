from fastapi import APIRouter
from services import health_check, chat as chat_service
from schemas import ApiResponse, ChatRequest

router = APIRouter()


@router.get(
    "/health",
    response_model=ApiResponse
)
async def health() -> ApiResponse:
    return await health_check()


@router.post(
    "/chat",
    response_model=ApiResponse
)
async def chat(request: ChatRequest) -> ApiResponse:
    return await chat_service(request)