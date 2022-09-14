from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
BLOG_NAME = os.getenv("BLOG_NAME")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", None)
