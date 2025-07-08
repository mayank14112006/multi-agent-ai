import subprocess
import json

def classify_intent(text):
    prompt = f"Classify the intent (search / generate / task) for: '{text}'"
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    response = result.stdout.decode("utf-8").lower()
    if "search" in response:
        return "search"
    elif "generate" in response or "code" in response:
        return "generate"
    elif "reminder" in response or "task" in response:
        return "task"
    else:
        return "unknown"