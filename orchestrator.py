from agents.intent_classifier import classify_intent
from agents.search_agent import handle_search
from agents.answer_agent import handle_generation
from agents.task_executor import handle_task

def route_input(user_input):
    intent = classify_intent(user_input)
    if intent == "search":
        return handle_search(user_input)
    elif intent == "generate":
        return handle_generation(user_input)
    elif intent == "task":
        return handle_task(user_input)
    else:
        return "Sorry, I couldn't understand your request."
