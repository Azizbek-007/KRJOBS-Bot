from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp
from utils.misc import rate_limit
from keyboards.default import menu
# from utils.db_api import User
# import logging


@rate_limit(limit=10)
@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer(f"Sálem {message.from_user.first_name}! Ózińizge kerekli bólimdi tańlań",
        reply_markup=menu)

@dp.message_handler(IsPrivate(), commands=['developer'])
async def bot_start(message: types.Message):
    await message.answer("👨‍💻 @Azizbek_Berdimuratov")