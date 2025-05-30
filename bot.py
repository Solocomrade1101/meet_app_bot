import os
import requests
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"
WEBHOOK_PATH = f"/webhook/{TOKEN}"

app = Flask(__name__)

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = request.get_json()
    message = update.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if text == "/start":
        payload = {
            "chat_id": chat_id,
            "photo": "https://fvmmnwoivowyilwyuqyh.supabase.co/storage/v1/object/public/events-images//Frame%202147223760.png",
            "caption": "Привет! На связи митапчик 🖤\nЗдесь мы собираем анонсы самых интересных событий околодизайна...",
            "reply_markup": {
                "inline_keyboard": [[
                    {
                        "text": "Смотреть события",
                        "web_app": {"url": "https://solocomrade1101.github.io/meet_app"}
                    }
                ]]
            }
        }
        requests.post(f"{URL}/sendPhoto", json=payload)

    return "ok", 200


@app.route("/")
def set_webhook():
    render_url = os.getenv("RENDER_EXTERNAL_URL")
    webhook_url = f"{render_url}{WEBHOOK_PATH}"
    response = requests.get(f"{URL}/setWebhook", params={"url": webhook_url})
    return f"Webhook set: {response.json()}", 200

