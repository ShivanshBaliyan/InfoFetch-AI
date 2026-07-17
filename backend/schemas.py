from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any = None

class ChatRequest(BaseModel):
    message: str


class ChatData(BaseModel):
    reply: str