from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Utility function to send WhatsApp message
def send_whatsapp_message(phone, message):
    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )

    msg = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Twilio Sandbox Number
        to=f'whatsapp:{phone}'
    )

    return msg.sid


# Route to send WhatsApp messages
@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')

    # Compose message if only name is provided
    if not message and name:
        message = f"Hi {name}, thanks for submitting the form! 🚀"
    elif not message:
        return jsonify({"error": "Missing message or name to generate message."}), 400

    try:
        sid = send_whatsapp_message(phone, message)
        return jsonify({"message_sid": sid, "status": "sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
