from enum import Enum


class Intent(Enum):
    GREETING = "greeting"
    CRICKET = "cricket"
    UNKNOWN = "unknown"


class CricketQuery(Enum):
    LIVE_MATCHES = "live_matches"
    PLAYER = "player"
    SCORE = "score"
    UPCOMING = "upcoming"
    UNKNOWN = "unknown"