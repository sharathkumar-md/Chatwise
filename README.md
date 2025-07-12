# ChatWise – WhatsApp Chatbot

ChatWise is a simple yet powerful chatbot that allows users to interact with an AI assistant over WhatsApp. It uses Flask for the backend, Twilio's WhatsApp Sandbox for messaging, and Together.ai's API for AI responses.

## Features

- Chat with an AI assistant via WhatsApp
- Uses Together.ai's LLaMA-3 model for responses
- Lightweight and easy to run locally
- No deployment required (uses Cloudflare Tunnel for public access)

## Technologies Used

- Python 3
- Flask
- Twilio WhatsApp Sandbox
- Together.ai API
- Cloudflare Tunnel
- dotenv

---

## Getting Started

Follow these steps to set up and use ChatWise:

### 1. Clone the Repository

git clone https://github.com/your-username/chatwise.git
cd chatwise

### 2. Set Up the Environment

Create and activate a virtual environment

- **On Windows:**

    python -m venv env
    env\Scripts\activate

- **On Mac/Linux:**

    python3 -m venv env
    source env/bin/activate

**Install the required packages:**
pip install -r requirements.txt


### 3. Add Your Together API Key

Create a `.env` file in the project root and add your Together API key:

TOGETHER_API_KEY=your_together_api_key_here

You can get your API key from [Together.ai API Keys](https://api.together.xyz/settings/api-keys)

    Note: You can integrate any other API of your choice

### 4. Start the Flask App

Run the Flask application:
python app.py

### 5. Create a Public Tunnel

Open a new terminal and run:

cloudflared tunnel --url http://localhost:5000  
<pre> Replace http://localhost:5000 with your local server’s URL </pre>

Copy the generated `https://...trycloudflare.com` URL.

### 6. Set Up Twilio Sandbox

1. Sign in to the [Twilio Console](https://www.twilio.com/console).
2. Go to **Messaging > Try it Out > Send a WhatsApp Message**.
3. Join the sandbox by sending the join code to the Twilio-provided number.
4. Under **"When a message comes in"**, set your webhook URL to:

     https://your-cloudflared-url/webhook

     (Replace `your-cloudflared-url` with the URL)  
     Choose **POST** as the method.

### 7. Start Chatting!

Send a message (like "hello") to the Twilio Sandbox number. You should receive a response from the AI assistant.

---

## File Structure

```
chatwise/
├── app.py               # Flask app
├── bot.py               # AI logic using Together API
├── templates/
│   └── index.html       # Home page
├── .env                 # Contains Together API key
├── requirements.txt     # Python dependencies
```

## Notes

- **Purpose:** This project is for development and learning. For production, secure your API and use proper hosting.


## License

This project is open-source under the MIT License.

## Acknowledgements

- Twilio WhatsApp Sandbox
- Together.ai
- Flask
- Cloudflare Tunnel

