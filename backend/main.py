from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import ChatRequest
from backend.chatbot import get_bot_response

app = FastAPI(title="North Star Support Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "North Star Support Bot API is running!"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    response, handoff = get_bot_response(request.message)

    return {
        "response": response,
        "handoff": handoff
    }