import httpx

from config import (
    CRICKET_API_BASE_URL,
    CRICKET_API_KEY,
)


async def get_current_matches() -> dict:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/currentMatches",
            params={
                "apikey": CRICKET_API_KEY,
                "offset": 0,
            },
        )

        response.raise_for_status()

        return response.json()


async def search_players(name: str) -> dict:
    """Search players by name."""

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/players",
            params={
                "apikey": CRICKET_API_KEY,
                "offset": 0,
                "search": name,
            },
        )
        response.raise_for_status()
        return response.json()


async def get_player_info(player_id: str) -> dict:
    """Fetch detailed information for a player."""

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/players_info",
            params={
                "apikey": CRICKET_API_KEY,
                "id": player_id,
            },
        )
        response.raise_for_status()
        return response.json()
    

async def get_match_info(match_id: str) -> dict:
    """Fetch detailed information about a match."""

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/match_info",
            params={
                "apikey": CRICKET_API_KEY,
                "offset": 0,
                "id": match_id,
            },
        )

        response.raise_for_status()
        return response.json()


async def search_series(name: str) -> dict:
    """Search cricket series by name."""

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/series",
            params={
                "apikey": CRICKET_API_KEY,
                "offset": 0,
                "search": name,
            },
        )

        response.raise_for_status()
        return response.json()


async def get_series_info(series_id: str) -> dict:
    """Fetch detailed information about a series."""

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/series_info",
            params={
                "apikey": CRICKET_API_KEY,
                "offset": 0,
                "id": series_id,
            },
        )

        response.raise_for_status()
        return response.json()


async def get_upcoming_matches() -> dict:
    """
    Return all matches.

    Upcoming matches can later be filtered in services.py
    based on match status or date.
    """

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{CRICKET_API_BASE_URL}/matches",
            params={
                "apikey": CRICKET_API_KEY,
                "offset": 0,
            },
        )

        response.raise_for_status()
        return response.json()


async def get_points_table():
    raise NotImplementedError(
        "Points Table endpoint is not available in the current API documentation."
    )


async def get_fantasy_squad():
    raise NotImplementedError(
        "Fantasy Squad endpoint is not available in the current API documentation."
    )