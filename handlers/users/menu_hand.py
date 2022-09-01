from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import choice
from loader import dp, CHANNEL_ID, bot
from keyboards.default import menu
from filters import IsPrivate

@dp.message_handler(IsPrivate(), text="❌ Bıykarlaw", state='*')
async def cancel_(message: types.Message, state: FSMContext):
    await state.finish()
    text = '❌ Biykar etildi. Siz tiykarǵı menyudasiz.'
    await message.answer(text, reply_markup=menu)

@dp.message_handler(IsPrivate(), text="✅ Tastıyıqlaw", state='*')
async def verify_(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = message.from_user.id
    await bot.send_message(CHANNEL_ID, user_data['ok'], reply_markup=choice(user_id))
    text = 'Sizdiń vakansiyaniz maǵlıwmatları moderatorlarga jiberildi, jaqın arada tekseriwlerden keyin sizge xabar jiberemiz'
    await message.answer(text, reply_markup=menu)