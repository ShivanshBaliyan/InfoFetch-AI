import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "")
print(f"BASE_URL = {BASE_URL!r}")

client = httpx.Client(base_url=BASE_URL)


def get_health():
    response = client.get("/health")
    response.raise_for_status()
    return response.json()


def send_message(message: str):
    response = client.post(
        "/chat",
        json={"message": message}
    )
    response.raise_for_status()
    return response.json()


def close_client():
    client.close()