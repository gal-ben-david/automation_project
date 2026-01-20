import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.zara.com/il/en/")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER = os.getenv("BROWSER", "chromium")
TIMEOUT = int(os.getenv("TIMEOUT", "10000"))
LOCALE = os.getenv("LOCALE", "en-US")
