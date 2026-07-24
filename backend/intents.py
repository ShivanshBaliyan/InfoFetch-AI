from enum import Enum


class Intent(Enum):
    GREETING = "greeting"
    CRICKET = "cricket"
    UNKNOWN = "unknown"


class CricketQuery(Enum):
    LIVE_MATCHES = "live_matches"
    PLAYER_INFO = "player_info"
    MATCH_INFO = "match_info"
    UPCOMING_MATCHES = "upcoming_matches"
    SERIES_SEARCH = "series_search"
    SERIES_INFO = "series_info"
    FANTASY_SQUAD = "fantasy_squad"
    POINTS_TABLE = "points_table"
    UNKNOWN = "unknown"