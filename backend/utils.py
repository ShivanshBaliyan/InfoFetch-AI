import re


def extract_player_name(message: str) -> str:
    """
    Extract the player's name from a user message.
    """

    message = message.lower().strip()

    patterns = [
        r"^tell me about\s+",
        r"^who is\s+",
        r"^show details for\s+",
        r"^show player\s+",
        r"^player\s+",
        r"^information about\s+",
        r"^details about\s+",
    ]

    for pattern in patterns:
        message = re.sub(pattern, "", message)

    return message.strip().title()


def extract_match_name(message: str) -> str:
    prefixes = [
        "match",
        "match score",
        "score",
        "scorecard",
        "result",
        "details of",
        "show match",
    ]

    message = message.lower().strip()

    for prefix in prefixes:
        if message.startswith(prefix):
            message = message[len(prefix):].strip()

    return message


def extract_series_name(message: str) -> str:
    prefixes = [
        "series",
        "tournament",
        "league",
        "tell me about",
        "show series",
    ]

    message = message.strip()

    lower = message.lower()

    for prefix in prefixes:
        if lower.startswith(prefix):
            message = message[len(prefix):].strip()
            break

    return message


def extract_query(message: str) -> str:
    message = message.lower()

    prefixes = [
        "tell me about",
        "information about",
        "details of",
        "who is",
        "show player",
        "show series",
        "player",
        "series",
        "league",
        "tournament",
    ]

    for prefix in prefixes:
        if message.startswith(prefix):
            message = message[len(prefix):].strip()
            break

    return message



