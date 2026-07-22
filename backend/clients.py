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