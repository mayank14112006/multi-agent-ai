# 🧠 Multi-Agent AI Chat System

An interactive, lightweight, multi-agent AI system built with FastAPI, Ollama (Mistral), and LangChain—offering memory-enabled continuous chat similar to ChatGPT!

🚀 Live Demo-Style Frontend | 🔍 Search Agent | 🧠 Memory Agent | 🤖 Local LLM Responses

---

## ✨ Features

- 🔁 Continuous, context-aware chat with per-user memory
- 🧩 Modular architecture with Search Agent + Answer Agent
- ⚡ Fast and offline-capable using Ollama (Mistral)
- 🌐 Sleek ChatGPT-style frontend (HTML/JS)
- 📁 Document-based retrieval support via LangChain

---

## 📸 Preview

> (Screenshot placeholder if needed)

---

## 📦 Tech Stack

- 🐍 Python 3.10+
- 🧠 [Ollama](https://ollama.com) + Mistral for local LLM inference
- 🔗 [LangChain](https://www.langchain.com) for vector search (with Chroma)
- ⚡ [FastAPI](https://fastapi.tiangolo.com) for backend
- 🌐 HTML + CSS + JS for frontend

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/multi-agent-ai-chat.git
cd multi-agent-ai-chat
```

2. Set up the Python environment:

```bash
python -m venv venv
# Activate virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

3. Install Ollama and load the model:
   Download Ollama from https://ollama.com/download, then run:

```bash
ollama run mistral
```

4. Start the FastAPI backend:

```bash
uvicorn main:app --reload
```

5. Run the chat interface:
   Open `frontend.html` in your browser.

---

📂 Project Structure

```plaintext
multi-agent-ai-chat/
├── agents/
│   ├── search_agent.py      # Retrieves context from documents
│   └── answer_agent.py      # LLM response with memory
├── chat_memory.py           # Per-user memory system
├── main.py                  # FastAPI app routes
├── frontend.html            # ChatGPT-style interface
├── requirements.txt         # Dependencies
└── README.md
```

---

📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| ...    | ...      | ...         |



Sample request:

```json
{
  "user_id": "user1",
  "question": "What is Gemini?"
}
```

Customization Ideas:
- Store memory in Redis or SQLite
- Allow uploading custom PDFs or documents
- Add streaming responses
- Implement a user login system

License:
MIT License © 2025 Mayank Goel
