import threading
import time
import requests
from datetime import datetime
from flask import Flask

app = Flask(__name__)

# 🔴 СПИСОК URL ДЛЯ САМОПИНГА
SELF_URLS = [
    "https://overprotein.onrender.com",
    "https://requests-site.onrender.com",
    "https://shoira.onrender.com",
    "https://qexdy.onrender.com",
    "https://tg-instagram-youtube-bot.onrender.com",
]

INTERVAL = 60  # 15 минут


def self_ping():
    while True:
        for url in SELF_URLS:
            try:
                r = requests.get(url, timeout=10)
                print(f"[{datetime.now()}] Self-ping OK | {url} | {r.status_code}")
            except Exception as e:
                print(f"[{datetime.now()}] Self-ping ERROR | {url} | {e}")

        time.sleep(INTERVAL)


@app.route("/")
def home():
    return "Service is alive", 200


if __name__ == "__main__":
    threading.Thread(target=self_ping, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
