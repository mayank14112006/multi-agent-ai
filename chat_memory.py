# chat_memory.py

# Simple in-memory dictionary to store conversation per user (basic demo only)
user_chats = {}

def get_chat_history(user_id: str) -> list[dict]:
    return user_chats.get(user_id, [])

def add_message(user_id: str, role: str, content: str):
    if user_id not in user_chats:
        user_chats[user_id] = []
    user_chats[user_id].append({"role": role, "content": content})

def clear_chat(user_id: str):
    user_chats[user_id] = []
