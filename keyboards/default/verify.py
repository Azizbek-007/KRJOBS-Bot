from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

verify = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tastıyıqlaw")
        ],
        [
            KeyboardButton(text="❌ Bıykarlaw")
        ]
    ],
    resize_keyboard=True
)