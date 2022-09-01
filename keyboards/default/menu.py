from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📢 Vakansiya jaylastırıw")
        ],
        [
            KeyboardButton(text="📄 Rezyume jaylastırıw")  
        ]
    ],
    resize_keyboard=True
)
