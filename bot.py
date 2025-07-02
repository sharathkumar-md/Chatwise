import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
print("Together API Key:", TOGETHER_API_KEY)


if not TOGETHER_API_KEY:
    print("TOGETHER_API_KEY not found. Please check your .env file.")
else:
    print("TOGETHER_API_KEY loaded.")

def generate_reply(message):
    try:
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "meta-llama/Llama-3-8b-chat-hf",  # You can switch to another Together-supported model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            "max_tokens": 100,
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an error for HTTP 4xx/5xx

        result = response.json()

        if "choices" in result and result["choices"]:
            return result["choices"][0]["message"]["content"].strip()
        else:
            print(" Unexpected response structure:", result)
            return "Sorry, I couldn't understand that."

    except requests.exceptions.HTTPError as http_err:
        print(f" HTTP error occurred: {http_err} - Response: {response.text}")
        return "Authentication failed. Check API key or model name."
    except Exception as e:
        print(f" Together API error: {e}")
        return "Sorry, I had trouble generating a response."
