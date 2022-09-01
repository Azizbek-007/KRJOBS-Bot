import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
GLOBAL_CHANNEL_ID = os.getenv("GLOBAL_CHANNEL")
admins = [
    5356014595,
]

allowed_users = [
    000000000,
]

ip = os.getenv("ip")
