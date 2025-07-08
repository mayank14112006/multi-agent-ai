# app_main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agents.search_agent import search
from agents.answer_agent import generate_answer
from chat_memory import clear_chat

app = FastAPI()

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str
    user_id: str

@app.post("/ask")
async def ask_question(data: QueryRequest):
    query = data.question
    user_id = data.user_id
    chunks = search(query)
    response = generate_answer(user_id, query, chunks)
    return {"answer": response}

@app.post("/reset")
async def reset_chat(data: QueryRequest):
    clear_chat(data.user_id)
    return {"message": "Chat reset."}