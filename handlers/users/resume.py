from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import cancel, verify
from states import Resume
from loader import dp, GLOBAL_CHANNEL_ID, bot
from filters import IsPrivate

@dp.message_handler(IsPrivate(), text="📄 Rezyume jaylastırıw")
async def get_button_one_resume(message: types.Message, state: FSMContext):
    await state.update_data(type="#Rezyume")
    text = "1. Famılıya hám atıńızdı kiritiń."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.fullname.set()

@dp.message_handler(state=Resume.fullname)
async def fullname_(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    text = "2. Jasıńızdı kiritiń."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.brithday)
async def brithday_(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    text = "3. Uqıplarıńızdı kiritiń."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.can)
async def can_(message: types.Message, state: FSMContext):
    await state.update_data(talents=message.text)
    text = "4. Neshe jıllıq tájiriybeniz bar?"
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.experience)
async def experience_(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    text = "5. Telegram adresinizdı kiritiń."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.telegram)
async def telegram_(message: types.Message, state: FSMContext):
    await state.update_data(telegram=message.text)
    text = "6. Telefon nomeriniz."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.contact)
async def contact_(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    text = "7. Aymaǵıńızdı kiritiń."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.live)
async def salary_(message: types.Message, state: FSMContext):
    await state.update_data(live=message.text)
    text = "💰 Mıynet haqın belgileń."
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.salary)
async def salary_(message: types.Message, state: FSMContext):
    await state.update_data(salary=message.text)
    text = "Maqsetińiz"
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Resume.next()

@dp.message_handler(state=Resume.goal)
async def goal_(message: types.Message, state: FSMContext):
    await state.update_data(goal=message.text)
    user_data = await state.get_data()
    CHANNEL = await bot.get_chat(GLOBAL_CHANNEL_ID)
    text = f'''
{user_data['type']}

<b>👨‍💻FAA:</b> {user_data['fullname']}
<b>🗓Jas:</b> {user_data['age']}
<b>📄Uqıplarım:</b> {user_data['talents']}
<b>📈Tájiriybe:</b> {user_data['experience']}
<b>🔵 Telegram:</b> {user_data['telegram']}
<b>☎️ Baylanıs:</b> {user_data['contact']}
<b>🌐 Aymaq:</b> {user_data['live']}
<b>💰Aylıq kútim:</b> {user_data['salary']}
<b>💫 Maqset:</b> {user_data['goal']}

👉🏻 Kanalǵa jazılıw @{CHANNEL.username}
    '''
    await state.finish()
    await state.update_data(ok=text)
    await message.answer(text, 'html')
    await message.answer('Barlıq maǵlıwmatlar tuwrı kiritilgen bolsa " ✅ Tastıyıqlaw" tuymesin basıń.', reply_markup=verify)



