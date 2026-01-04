import time
import requests
from datetime import datetime

URL = "https://overprotein.shop/"
INTERVAL = 15 * 60  # 15 минут в секундах

while True:
    try:
        response = requests.get(URL, timeout=10)
        print(f"[{datetime.now()}] Статус: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Ошибка: {e}")

    time.sleep(INTERVAL)
