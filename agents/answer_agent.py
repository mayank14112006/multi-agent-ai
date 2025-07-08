# answer_agent.py

import subprocess
from chat_memory import get_chat_history, add_message

def ask_mistral(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode()

def generate_answer(user_id: str, user_query: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    history = get_chat_history(user_id)

    history_text = ""
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        history_text += f"{role}: {msg['content']}\n"

    prompt = f"""
You are an intelligent assistant. Use the following document context and conversation history to answer the user's new question.

Document Context:
{context}

Conversation:
{history_text}
User: {user_query}
Assistant:
"""

    response = ask_mistral(prompt)
    add_message(user_id, "user", user_query)
    add_message(user_id, "assistant", response.strip())
    return response.strip()
