import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = 0

while True:
    response = requests.get(f"{URL}/getUpdates", params={"offset": last_update_id + 1})
    updates = response.json()

    for update in updates.get("result", []):
        last_update_id = update["update_id"]

        message = update.get("message", {})
        text = message.get("text", "")
        chat_id = message.get("chat", {}).get("id")

        if text == "/start":
            payload = {
                "chat_id": chat_id,
                "photo": "https://fvmmnwoivowyilwyuqyh.supabase.co/storage/v1/object/public/events-images//Frame%202147223760.png",
                "caption": "Привет! На связи митапчик 🖤\nЗдесь мы собираем анонсы самых интересных событий околодизайна: конференции, митапы, воркшопы, встречи и многое другое. Цель — создать единое пространство дизайн-активностей, чтобы быть в курсе, что посмотреть и куда сходить.",
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

    time.sleep(1)
