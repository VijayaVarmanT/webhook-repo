from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("✅ Webhook received:")
    print(data)
    return jsonify({'message': 'Received'}), 200

@app.route('/webhook', methods=['GET'])
def test_webhook():
    return "🟢 Webhook endpoint is working (GET)", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
