import httpx 
from schemas import (
    ApiResponse, 
    ChatData, 
    ChatRequest
)

from intents import (
    Intent, 
    CricketQuery
)

from clients import (
    get_current_matches,
    search_players,
    get_player_info,
    get_match_info,
    search_series,
    get_series_info,
    get_upcoming_matches,
)

from formatters import (
    format_player,
    format_upcoming_matches,
    format_match_info,
    format_series_list,
    format_series_info,
)

from utils import (
    extract_query,
    extract_match_name,
    extract_series_name,
)


async def health_check() -> ApiResponse:
    return ApiResponse(
        success=True,
        message="Application is running.",
        data={
            "status": "healthy"
        }
    )


def detect_intent(message: str) -> Intent:
    message = message.lower()
    words = message.split()

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
        "series",
        "points",
        "table",
        "fantasy",
        "dream11",
        "squad",
        "league",
        "asia",
        "cup",
        "world",
        "champions",
        "trophy",
    }

    player_phrases = (
        "who is",
        "show player",
    )

    series_phrases = (
        "tell me about",
        "information about",
        "show series",
        "details of",
    )

    if any(word in greeting_keywords for word in words):
        return Intent.GREETING

    if any(word in cricket_keywords for word in words):
        return Intent.CRICKET

    if any(message.startswith(phrase) for phrase in player_phrases):
        return Intent.CRICKET

    if any(message.startswith(phrase) for phrase in series_phrases):
        return Intent.CRICKET

    return Intent.UNKNOWN


def detect_cricket_query(message: str) -> CricketQuery:
    message = message.lower()

    live_keywords = {
        "live",
        "current",
        "ongoing",
        "match",
        "matches",
    }

    score_keywords = {
        "score",
        "scores",
        "scorecard",
        "result",
    }

    upcoming_keywords = {
        "next",
        "upcoming",
        "fixture",
        "fixtures",
    }

    series_keywords = {
        "series",
        "league",
        "tournament",
        "ipl",
        "asia",
        "world",
        "champions",
        "cup",
        "trophy",
    }

    points_keywords = {
        "points",
        "table",
        "standings",
    }

    fantasy_keywords = {
        "fantasy",
        "dream11",
        "squad",
    }

    player_phrases = (
        "who is",
        "show player",
    )

    info_phrases = (
        "tell me about",
        "information about",
        "details of",
        "show",
    )
    

    if any(message.startswith(p) for p in player_phrases):
        return CricketQuery.PLAYER_INFO

    if any(keyword in message for keyword in score_keywords):
        return CricketQuery.MATCH_INFO

    if any(keyword in message for keyword in upcoming_keywords):
        return CricketQuery.UPCOMING_MATCHES

    if any(message.startswith(p) for p in info_phrases):
        return CricketQuery.SERIES_INFO

    if any(keyword in message for keyword in series_keywords):
        return CricketQuery.SERIES_SEARCH

    if any(keyword in message for keyword in points_keywords):
        return CricketQuery.POINTS_TABLE

    if any(keyword in message for keyword in fantasy_keywords):
        return CricketQuery.FANTASY_SQUAD

    if any(keyword in message for keyword in live_keywords):
        return CricketQuery.LIVE_MATCHES

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

    elif query == CricketQuery.MATCH_INFO:
        return await match_response(message)

    elif query == CricketQuery.UPCOMING_MATCHES:
        return await upcoming_matches_response()

    elif query == CricketQuery.PLAYER_INFO:
        return await player_response(message)

    elif query == CricketQuery.SERIES_SEARCH:
        return await series_response(message)

    elif query == CricketQuery.SERIES_INFO:
        return await series_info_response(message)

    elif query == CricketQuery.FANTASY_SQUAD:
        return "🧢 Fantasy squad feature coming soon."

    elif query == CricketQuery.POINTS_TABLE:
        return "📊 Points table feature coming soon."

    # query_text = extract_query(message)

    query_text = extract_query(message)

    print("Original :", message)
    print("Searching:", query_text)

    search = await search_players(query_text)

    print(search)

    # search = await search_players(query_text)

    players = search.get("data", [])

    if players:
        return await player_response_by_id(players[0]["id"])

    return unknown_response()


def unknown_response() -> str:
    return "Sorry, I didn't understand your request."


async def chat(request: ChatRequest) -> ApiResponse:
    intent = detect_intent(request.message)

    if intent == Intent.GREETING:
        reply = greeting_response()

    else:
        # Let cricket_response() try to handle all non-greeting messages
        reply = await cricket_response(request.message)

    return ApiResponse(
        success=True,
        message="Response generated successfully.",
        data=ChatData(reply=reply)
    )


async def player_response_by_id(player_id: str) -> str:
    try:
        player_result = await get_player_info(player_id)

    except httpx.TimeoutException:
        return "The cricket API took too long to respond."

    player = player_result.get("data")

    if not player:
        return "Unable to fetch player details."

    return format_player(player)


async def player_response(message: str) -> str:
    player_name = extract_query(message)

    search_result = await search_players(player_name)

    players = search_result.get("data", [])

    if not players:
        return f"No player found matching '{player_name}'."

    player_id = players[0]["id"]

    return await player_response_by_id(player_id)


async def upcoming_matches_response() -> str:
    matches = await get_upcoming_matches()
    return format_upcoming_matches(matches)


async def match_response(message: str) -> str:
    match_name = extract_match_name(message)

    matches = await get_upcoming_matches()

    for match in matches.get("data", []):
        if match_name.lower() in match.get("name", "").lower():
            match_id = match["id"]

            result = await get_match_info(match_id)

            if result.get("data"):
                return format_match_info(result["data"])

    return f"No match found matching '{match_name}'."


async def series_response(message: str) -> str:
    series_name = extract_series_name(message)

    result = await search_series(series_name)

    return format_series_list(result)


async def series_info_response(message: str) -> str:
    query = extract_query(message)

    # Try series 
    series_result = await search_series(query)

    series_list = series_result.get("data", [])

    if series_list:
        series_id = series_list[0]["id"]

        result = await get_series_info(series_id)

        if result.get("data"):
            return format_series_info(result["data"])


    # Try player 
    player_result = await search_players(query)

    players = player_result.get("data", [])

    if players:
        player_id = players[0]["id"]

        return await player_response_by_id(player_id)

    return f"No player or series found matching '{query}'."

