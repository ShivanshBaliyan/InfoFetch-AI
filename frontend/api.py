import httpx
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "")

client = httpx.AsyncClient(base_url=BASE_URL)

async def get_health():
    response = await client.get("/health")
    response.raise_for_status()
    return response.json()
    

async def send_message(message: str):
    response = await client.post(
        "/chat",
        json={"message": message}
    )
    response.raise_for_status()
    return response.json()


# async def close_client():
#     await client.aclose()