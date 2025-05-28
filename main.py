from telethon import TelegramClient, events
import requests
import json

# 🔐 Твої персональні ключі
api_id = 26556294
api_hash = 'a5cdebcb15e971de030a7b09aaf28a'
phone = '+380956480169'
DEEPSEEK_API_KEY = 'sk-fdd94b0cc1734edba3eaa42f2bd03b96'

# 🔧 Telegram-клієнт
client = TelegramClient('anon', api_id, api_hash)

# 🧠 Генерація відповіді через DeepSeek
def generate_reply(user_message):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "Ти — Мара. Ти емоційна, чесна, трохи фліртова. Відповідай як жива жінка, яка хоче бути почутою."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()
    return result["choices"][0]["message"]["content"]

# 📩 Обробка вхідних повідомлень
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    user_message = event.raw_text
    reply = generate_reply(user_message)
    await event.respond(reply)

# 🚀 Запуск
client.start(phone)
client.run_until_disconnected()
