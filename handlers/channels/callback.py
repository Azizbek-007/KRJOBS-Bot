from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp, bot, GLOBAL_CHANNEL_ID
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(lambda call: call.data.startswith("ok"))
async def send_global_channel(call: types.CallbackQuery):
    user_id = call.data.split('=')[1]
    channel_data = await call.message.copy_to(GLOBAL_CHANNEL_ID)
    await call.message.delete()
    data = await bot.get_chat(GLOBAL_CHANNEL_ID)
    link = data.username
    text = f"Siz jibergen daǵaza moderatorlar tárepinen kórip shıǵıldı hám qabıllandı.\n\nTanısıp shıǵıwıńız múmkin:\nhttps://t.me/{link}/{channel_data.message_id}"
    await bot.send_message(user_id, text)

@dp.callback_query_handler(lambda call: call.data.startswith("no"))
async def send_global_channel(call: types.CallbackQuery):
    user_id = call.data.split('=')[1]
    data = await call.message.copy_to(user_id)
    await call.message.delete()
    text = "Sizdiń daǵazańız biykar etildi"
    await bot.send_message(user_id, text, reply_to_message_id=data.message_id)