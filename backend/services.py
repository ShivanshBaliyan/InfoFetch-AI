from schemas import ApiResponse, ChatData, ChatRequest
from intents import Intent, CricketQuery
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
        "fixture",
        "fixtures",
        "player",
        "batsman",
        "bowler",
        "captain",
        "kohli",
        "rohit",
    }

    if any(word in greeting_keywords for word in words):
        return Intent.GREETING

    if any(word in cricket_keywords for word in words):
        return Intent.CRICKET

    return Intent.UNKNOWN


def detect_cricket_query(message: str) -> CricketQuery:
    words = message.lower().split()

    live_keywords = {"live", "match", "matches", "current"}
    score_keywords = {"score", "scores", "result"}
    upcoming_keywords = {"next", "upcoming", "fixture", "fixtures"}
    player_keywords = {
        "player",
        "batsman",
        "bowler",
        "captain",
        "kohli",
        "rohit",
    }

    if any(word in live_keywords for word in words):
        return CricketQuery.LIVE_MATCHES

    if any(word in score_keywords for word in words):
        return CricketQuery.SCORE

    if any(word in upcoming_keywords for word in words):
        return CricketQuery.UPCOMING

    if any(word in player_keywords for word in words):
        return CricketQuery.PLAYER

    return CricketQuery.UNKNOWN


def greeting_response() -> str:
    return "Hello! 👋 How can I help you today?"


def format_matches(matches: dict) -> str:
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


async def cricket_response(message: str) -> str:
    query = detect_cricket_query(message)

    if query == CricketQuery.LIVE_MATCHES:
        matches = await get_current_matches()
        return format_matches(matches)

    elif query == CricketQuery.SCORE:
        return "🏏 Score feature coming soon."

    elif query == CricketQuery.UPCOMING:
        return "📅 Upcoming matches feature coming soon."

    elif query == CricketQuery.PLAYER:
        return "👤 Player information feature coming soon."

    else:
        return (
            "Please ask about:\n"
            "• Live matches\n"
            "• Match scores\n"
            "• Upcoming matches\n"
            "• Cricket players"
        )


def unknown_response() -> str:
    return "Sorry, I didn't understand your request."


async def chat(request: ChatRequest) -> ApiResponse:
    intent = detect_intent(request.message)

    if intent == Intent.GREETING:
        reply = greeting_response()

    elif intent == Intent.CRICKET:
        reply = await cricket_response(request.message)

    else:
        reply = unknown_response()

    return ApiResponse(
        success=True,
        message="Response generated successfully.",
        data=ChatData(reply=reply)
    )