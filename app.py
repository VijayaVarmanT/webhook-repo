from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Server is up"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        payload = request.get_json()
        print("✅ Webhook received:")
        print(payload)
        return jsonify({'message': 'Received'}), 200
    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/webhook', methods=['GET'])
def test_webhook():
    return "🟢 Webhook GET works", 200

if __name__ == '__main__':
    app.run(port=5000)
