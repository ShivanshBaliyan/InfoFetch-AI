from schemas import ApiResponse, ChatRequest


async def health_check() -> ApiResponse:
    return ApiResponse(
        success=True,
        message="Application is running.",
        data={
            "status": "healthy"
        }
    )

async def chat(request: ChatRequest) -> ApiResponse:
    return ApiResponse(
        success=True,
        message="Response generated successfully",
        data={
            "reply": f"You said: {request.message}"
        }
    )