import os
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from bot import generate_reply

# Load .env
load_dotenv()

# Debug: print loaded API key (only the first 6 chars for safety)
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
print(f"✅ TOGETHER_API_KEY loaded: {TOGETHER_API_KEY[:6]}..." if TOGETHER_API_KEY else "❌ TOGETHER_API_KEY NOT found!")

# Debug: print all environment variables starting with 'TOGETHER'
for k, v in os.environ.items():
    if k.startswith('TOGETHER'):
        print(f"ENV {k} = {v}")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body')
    sender = request.form.get('From')

    print(f" Received from {sender}: {incoming_msg}")

    reply = generate_reply(incoming_msg)
    print(f" Replying with: {reply}")

    response = MessagingResponse()
    response.message(reply)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
