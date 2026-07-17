import httpx
from dotenv import load_dotenv
import os

load_dotenv()

# BASE_URL = "http://127.0.0.1:8000"
BASE_URL = os.getenv("BASE_URL", "")

async def get_health():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/health")
        response.raise_for_status()
        return response.json()