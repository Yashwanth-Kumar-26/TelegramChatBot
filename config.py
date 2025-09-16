import os
from dotenv import load_dotenv

load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Data storage (in-memory, can be expanded to DB later)
USER_SETTINGS = {}  # user_id: {'model': model_id}

# Bot settings
DEFAULT_MODEL = 'deepseek/deepseek-r1-0528-qwen3-8b:free'
SITE_URL = 'https://t.me/your_bot'
SITE_NAME = 'Telegram AI Chat Bot'
