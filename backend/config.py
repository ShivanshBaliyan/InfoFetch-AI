import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application Information
APP_NAME = "Website Data Chatbot API"
APP_VERSION = "1.0.0"

# External API Configuration
API_KEY = os.getenv("API_KEY", "")
BASE_URL = os.getenv("BASE_URL", "")