from schemas import ApiResponse


async def health_check() -> ApiResponse:
    return ApiResponse(
        success=True,
        message="Application is running.",
        data={
            "status": "healthy"
        }
    )