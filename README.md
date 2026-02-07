# AI-WAF: AI-Powered Web Application Firewall

**AI-WAF** is an AI-powered Web Application Firewall designed to protect AI-driven applications and web platforms from malicious user inputs. It analyzes prompts in real time, classifying them as **Benign**, **Suspicious**, or **Malicious**, and assigns a risk score to ensure safe and reliable operations.


## Demo

- **Frontend:** [Netlify Deployment URL](https://ai-waf.netlify.app/)  
- **Backend API:** [Railway Deployment URL](https://ai-waf-production.up.railway.app/)  

> Use the frontend to test prompts and see real-time risk analysis.

## Problem Statement

Modern AI and web applications are vulnerable to malicious inputs such as prompt injections, SQL injection patterns, XSS attacks, and policy bypass attempts. Traditional security rules often fail to detect these attacks effectively.


## Solution Overview

AI-WAF analyzes user prompts in real time using an AI model and provides structured responses. Workflow:

1. User enters prompt in frontend.  
2. Frontend sends POST request to backend API.  
3. Backend calls AI model to analyze intent.  
4. Response includes:
   - **Intent:** Benign, Suspicious, or Malicious  
   - **Risk Score:** Numerical risk level  
   - **Reason:** Explanation for classification  

This ensures AI and web applications are protected from malicious or unsafe inputs.


## Key Features

- Real-time prompt analysis  
- Dynamic risk scoring  
- Detection of prompt injection, XSS, and SQL injection patterns  
- Safe fallback handling for unparseable input  
- API-based backend for integration flexibility  
- Responsive frontend UI  


## System Architecture

Frontend (HTML/CSS/JS)
│
Backend (FastAPI)
│
AI Model (Groq)
│
JSON Response
|
Output

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, FastAPI  
- **AI Inference:** Groq LLM  
- **Hosting:** Netlify (Frontend), Railway (Backend)  


## Installation

1. Clone the repository:
```bash
git clone https://github.com/AyeshaIjazTabassum/AI-WAF.git
cd AI-WAF/backend
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage

- Run the backend:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- Open frontend/index.html in a browser or deploy via Netlify.
- Enter a prompt and click Analyze to see Intent, Risk Score and Reason.

## Environment Variables
- Create a .env file in backend/:
```bash
GROQ_API_KEY=your_actual_groq_api_key
```
> Important: Do not commit .env to GitHub. Add it to .gitignore.

## Flow Diagram
<img width="1536" height="1024" alt="AI-WAF workflow" src="https://github.com/user-attachments/assets/2a39708f-256d-4966-bb22-e489cb799aab" />

## System
<img width="1902" height="872" alt="Screenshot 2026-02-07 215244" src="https://github.com/user-attachments/assets/b05b0e31-6e05-40a2-b2bb-551f17e21bc8" />
