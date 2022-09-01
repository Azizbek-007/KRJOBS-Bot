from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
CHANNEL_ID = config.CHANNEL_ID
GLOBAL_CHANNEL_ID = config.GLOBAL_CHANNEL_ID