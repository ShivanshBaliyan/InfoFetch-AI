from schemas import ApiResponse, ChatData, ChatRequest
from intents import Intent
from clients import get_current_matches


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
    cricket_keywords = {
        "cricket",
        "match",
        "matches",
        "score",
        "scores",
        "ipl",
        "live",
    }

    if any(word in greeting_keywords for word in words):
        return Intent.GREETING

    if any(word in cricket_keywords for word in words):
        return Intent.CRICKET

    return Intent.UNKNOWN


def greeting_response() -> str:
    return "Hello! 👋 How can I help you today?"


def format_matches(matches: dict) -> str:
    """
    Convert the CricketData API response into
    a user-friendly text.
    """
    data = matches.get("data", [])

    if not data:
        return "No cricket matches found."

    lines = ["🏏 Current Cricket Matches\n"]

    for match in data[:5]:
        lines.append(f"📍 {match['name']}")
        lines.append(f"Status: {match['status']}")
        lines.append(f"Venue: {match['venue']}")

        scores = match.get("score", [])

        if scores:
            lines.append("Scores:")

            for inning in scores:
                lines.append(
                    f"• {inning['inning']}: "
                    f"{inning['r']}/{inning['w']} "
                    f"({inning['o']} overs)"
                )

        lines.append("")

    return "\n".join(lines)


async def cricket_response() -> str:
    matches = await get_current_matches()

    return format_matches(matches)


def unknown_response() -> str:
    return "Sorry, I didn't understand your request."


async def chat(request: ChatRequest) -> ApiResponse:
    intent = detect_intent(request.message)

    if intent == Intent.GREETING:
        reply = greeting_response()

    elif intent == Intent.CRICKET:
        reply = await cricket_response()

    else:
        reply = unknown_response()

    return ApiResponse(
        success=True,
        message="Response generated successfully.",
        data=ChatData(
            reply=reply
        )
    )