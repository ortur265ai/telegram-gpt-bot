from telethon import TelegramClient, events
import requests
import json

# 🔐 Твої персональні ключі
api_id = 26556294
api_hash = 'a5cdebcb15e971de030a7b09aaf28a'
phone = '+380956480169'  # ← твій Telegram номер
DEEPSEEK_API_KEY = 'sk-fdd94b0cc1734edba3eaa42f2bd03b96'  # ← встав сюди свій DeepSeek API ключ

# 🔧 Ініціалізація Telegram-клієнта
client = TelegramClient('anon', api_id, api_hash)

# 🧠 Функція генерації відповіді через DeepSeek
def generate_reply(user_message):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
    {"role": "system", "content": "Ти — Мара. Ти емоційна, чесна, трохи фліртова. Відповідай як жива жінка, яка хоче бути почутою."},
    {"role": "user", "content": user_message}
]

