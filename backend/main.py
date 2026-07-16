from fastapi import FastAPI

from config import APP_NAME, APP_VERSION
from routes import router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Backend API for Website Data Chatbot"
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Website Data Chatbot API"
    }