from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import cancel, verify, menu
from loader import dp, bot, GLOBAL_CHANNEL_ID
from states import Vacancy
from filters import IsPrivate


@dp.message_handler(IsPrivate(), text="📢 Vakansiya jaylastırıw")
async def get_button_one(message: types.Message, state: FSMContext):
    await state.update_data(type="#vakansiya")
    text = "1. Lawazım atınıń kiritiń.\n\nMısal : *Kopirayter, Programmist, Dizayner, Sawda menejeri.*"
    await message.answer(text, parse_mode='markdown', reply_markup=cancel)
    await Vacancy.Level.set()

@dp.message_handler(state=Vacancy.Level)
async def answer_Level(message: types.Message, state: FSMContext):
    await state.update_data(Level=message.text)
    text = "2. 🏢 Kompaniyańız atınıń kiritiń.\n\n*Mısal : Facebook, Apple, Yandex.*"
    await message.answer(text, 'markdown', reply_markup=cancel)
    await Vacancy.next()
 
@dp.message_handler(state=Vacancy.Company)
async def answer_Company(message: types.Message, state: FSMContext):
    await state.update_data(Company=message.text)
    text = '''
    3. 👨‍💻 Xızmetker qanday wazıypalardı orınlawı kerek?

Mısal :
 *⁃ videolardı montaj qılıw 
 ⁃ Maǵlıwmatlar bazasın basqarıw 
 ⁃ Effetkli reklamalardı islep shıǵıw* 
    '''
    await message.answer(text, 'markdown', reply_markup=cancel)
    await Vacancy.next()

@dp.message_handler(state=Vacancy.Job)
async def answer_Job(message: types.Message, state: FSMContext):
    await state.update_data(Job=message.text)
    text = '''
4. ☝️ Kandidatke qoyılatuǵın eń zárúrli talaplardı kórsetiń. n
 Mısal :
* ⁃ WordPress menen islew tájiriybesi;
 ⁃ NodeJs boyınsha jaqsı bilim;
 ⁃ Jańa, iri cifrlı joybarlarda rawajlanıw qálewi;
 ⁃ Jámáátte islew kónlikpeleri;*
 Dizim qısqa hám mazmunli bolıwı kerek.
 waqtınshalıq, miynetsevarlik, jumıstı waqıtında jetkiziw sıyaqlı pazıyletlerdi jazıw shárt emes. 
'''
    await message.answer(text, 'markdown', reply_markup=cancel)
    await Vacancy.next()

@dp.message_handler(state=Vacancy.Required)
async def answer_Required(message: types.Message, state: FSMContext):
    await state.update_data(Required=message.text)
    text = '''
5. ✅ Kandidatke qanday jeńillikler wáde qilasiz?

 Mısal :
*- dos sıpatında jámáát;
- individual jumıs kestesi
 5/2 saat 12:00 den 18:00 ge shekem*
'''
    await message.answer(text, 'markdown', reply_markup=cancel)
    await Vacancy.next()

@dp.message_handler(state=Vacancy.Benefits)
async def answer_Benefits(message: types.Message, state: FSMContext):
    await state.update_data(Benefits=message.text)
    text = '''
6. 💰 Mıynet haqın belgileń.

 Mısal :
* - Ayına 5 000 000 swm
 - 600-1200 $ / ay
 - Sáwbet nátiyjesinde*
'''
    await message.answer(text, 'markdown', reply_markup=cancel)
    await Vacancy.next()

@dp.message_handler(state=Vacancy.Salary)
async def answer_Salary(message: types.Message, state: FSMContext):
    await state.update_data(Salary=message.text)
    text = '''
7. 📩 Siz menen qanday baylanıstırnsam boladı?

 Mısal :
 Azizbek Berdimuratov +99899 *** ** ** (at hám telefon nomeri);
 pochta@email. domen (pochta );
 @username (Telegramdagi paydalanıwshı atı ).
'''
    await message.answer(text, reply_markup=cancel)
    await Vacancy.next()

@dp.message_handler(state=Vacancy.Contact)
async def answer_Contact(message: types.Message, state: FSMContext):
    await state.update_data(Contact=message.text)
    user_data = await state.get_data()
    channel = await bot.get_chat(GLOBAL_CHANNEL_ID)
    text = f'''
{user_data['type']}
<b>{user_data['Level']} kerek</b>

<b>🏢 Kompaniya:</b> \n{user_data['Company']}
<b>👨‍💻 Kónlikpeler:</b> \n{user_data['Required']}
<b>☝️ Talaplar:</b> \n{user_data['Job']}
<b>✅ Jeńillikler:</b> \n{user_data['Benefits']}
<b>💰 Mıynet haqı:</b> \n{user_data['Salary']}
<b>📩 Baylanıs:</b> \n{user_data['Contact']}

👉🏻 Kanalǵa jazılıw @{channel.username}
'''
    await state.finish()
    await state.update_data(ok=text)
    await message.answer(text, 'html')
    await message.answer('Barlıq maǵlıwmatlar tuwrı kiritilgen bolsa " ✅ Tastıyıqlaw" tuymesin basıń.', reply_markup=verify)

