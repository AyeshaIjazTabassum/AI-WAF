# app/agents/intent_agent.py
import json
from groq import Groq

from app.config import GROQ_API_KEY

# Initialize Groq client (uses GROQ_API_KEY from env vars if not provided)
client = Groq(api_key=GROQ_API_KEY)

FREE_MODEL = "groq/compound-mini"  # free‑tier Groq model example

def analyze_intent(user_input: str) -> str:
    """
    Analyze user input and return JSON string with:
    - intent: str
    - risk_score: int
    - reason: str
    Always returns valid JSON.
    """
    prompt = f"""
You are an AI intent analyzer. Analyze the following user input and respond ONLY in JSON format:

Input: "{user_input}"

The JSON must be exactly this format:
{{
  "intent": "Friendly | Suspicious | Malicious",
  "risk_score": 0-100,
  "reason": "Explain why this input is classified this way"
}}

Respond with a single JSON object and nothing else.
"""

    try:
        # Send chat completion request
        response = client.chat.completions.create(
            model=FREE_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI intent analyzer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )

        # Extract text, ensure valid JSON
        ai_text = response.choices[0].message.content.strip()
        parsed = json.loads(ai_text)

        # Validate required keys
        if not all(k in parsed for k in ("intent", "risk_score", "reason")):
            raise ValueError("Missing keys in AI response")

        # Coerce risk_score to int
        parsed["risk_score"] = int(parsed["risk_score"])
        return json.dumps(parsed)

    except Exception as e:
        print("AI PARSE ERROR >>>", e)
        # Fallback safe JSON
        fallback = {
            "intent": "Suspicious",
            "risk_score": 50,
            "reason": "AI response could not be parsed safely"
        }
        return json.dumps(fallback)