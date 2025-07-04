from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Webhook Server Live"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📦 Webhook received:", data)
    return jsonify({'status': 'Received'}), 200
