# dify_client.py
import os
import requests

# Get Dify API key from environment variable
DIFY_API_KEY = os.getenv("DIFY_API_KEY")  # Make sure this is set in docker-compose or locally
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

def ask_dify(question: str, user_id="user-1") -> str:
    """
    Send a user question to the Annapurna (Dify) chatbot
    and return the response as a string.
    """
    if not DIFY_API_KEY:
        return "⚠️ Dify API key not configured. Please set DIFY_API_KEY."

    headers = {"Authorization": f"Bearer {DIFY_API_KEY}"}
    payload = {
        "query": question,
        "inputs": {},           # Extra input fields if needed
        "response_mode": "blocking",
        "conversation_id": None, # Keep None to start a new conversation
        "user": user_id
    }

    try:
        response = requests.post(DIFY_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Return the chatbot's answer
        if "answer" in data and data["answer"]:
            return data["answer"]
        else:
            return "⚠️ No response from Annapurna. Try again."

    except requests.exceptions.RequestException as e:
        return f"❌ Error connecting to Annapurna: {str(e)}"
