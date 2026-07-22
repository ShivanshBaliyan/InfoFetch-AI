import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "InfoFetch AI"
APP_VERSION = "1.0.0"

CRICKET_API_KEY = os.getenv("CRICKET_API_KEY", "")
CRICKET_API_BASE_URL = os.getenv(
    "CRICKET_API_BASE_URL",
    "https://api.cricketdata.org/v1"
)