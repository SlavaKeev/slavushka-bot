from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

@app.route("/", methods=["POST"])
def alert():
    data = request.get_json()
    message = data.get("text", "⚠️ Пустое сообщение от TradingView")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)