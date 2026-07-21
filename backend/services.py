from schemas import ApiResponse, ChatData, ChatRequest
from intents import Intent


async def health_check() -> ApiResponse:
    return ApiResponse(
        success=True,
        message="Application is running.",
        data={
            "status": "healthy"
        }
    )


def detect_intent(message: str) -> Intent:
    words = message.lower().split()

    greeting_keywords = {"hi", "hello", "hey"}
    cricket_keywords = {"cricket", "match", "score", "ipl"}

    if any(word in greeting_keywords for word in words):
        return Intent.GREETING

    if any(word in cricket_keywords for word in words):
        return Intent.CRICKET

    return Intent.UNKNOWN


def greeting_response() -> str:
    return "Hello! 👋 How can I help you today?"


def cricket_response() -> str:
    return "🏏 Cricket support is coming soon."


def unknown_response() -> str:
    return "Sorry, I didn't understand your request."

async def chat(request: ChatRequest) -> ApiResponse:
    intent = detect_intent(request.message)
    print(f"Intent: {intent}")

    if intent == Intent.GREETING:
        reply = greeting_response()
    elif intent == Intent.CRICKET:
        reply = cricket_response()
    else:
        reply = unknown_response()

    return ApiResponse(
        success=True,
        message="Response generated successfully.",
        data=ChatData(reply=reply),
    )