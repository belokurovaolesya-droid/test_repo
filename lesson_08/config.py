import os

from dotenv import load_dotenv


load_dotenv()

BASE_URL = "https://ru.yougile.com"
TOKEN = os.getenv("YOUGILE_TOKEN")

if not TOKEN:
    raise ValueError(
        "Переменная окружения YOUGILE_TOKEN не установлена"
    )

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}