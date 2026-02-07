# import json
# from fastapi import FastAPI, HTTPException
# from app.schemas import PromptRequest, IntentResponse
# from app.agents.intent_agent import analyze_intent


# app = FastAPI(title="Solva AI WAF – Intent Analyzer")


# @app.get("/")
# def health_check():
#     return {"status": "Solva AI WAF is running"}


# @app.post("/analyze-intent", response_model=IntentResponse)
# def analyze_prompt(data: PromptRequest):
#     ai_raw = analyze_intent(data.prompt)

#     # Debug: log the raw AI response
#     print("RAW AI RESPONSE >>>", repr(ai_raw))

#     # Ensure valid JSON response
#     try:
#         parsed = json.loads(ai_raw)
        
#         # Validate that required keys exist
#         if not all(k in parsed for k in ("intent", "risk_score", "reason")):
#             raise ValueError("Missing required keys in AI response")
        
#         # Optional: ensure risk_score is numeric
#         parsed["risk_score"] = int(parsed.get("risk_score", 50))

#         return parsed

#     except Exception as e:
#         print("JSON PARSE ERROR >>>", e)
#         # Fallback safe response
#         return {
#             "intent": "Suspicious",
#             "risk_score": 50,
#             "reason": "AI response could not be parsed safely"
#         }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.schemas import PromptRequest, IntentResponse
from backend.app.agents.intent_agent import analyze_intent
import json

app = FastAPI(title="Solva AI WAF – Intent Analyzer")

# ✅ Enable CORS so frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:8001"] to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "Solva AI WAF is running"}

@app.post("/analyze-intent", response_model=IntentResponse)
def analyze_prompt(data: PromptRequest):
    ai_raw = analyze_intent(data.prompt)
    try:
        parsed = json.loads(ai_raw)
        return parsed
    except:
        return {
            "intent": "Suspicious",
            "risk_score": 50,
            "reason": "AI response could not be parsed safely"
        }
