# app/schemas.py
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class IntentResponse(BaseModel):
    intent: str
    risk_score: int
    reason: str