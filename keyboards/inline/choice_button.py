from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choice (user_id):
    return InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="✅ Tastıyıqlaw",
                                          callback_data=f"ok={user_id}"
                                      ),
                                      InlineKeyboardButton(
                                          text="❌ Bıykarlaw",
                                          callback_data=f"no={user_id}"
                                      ),
                                  ]

                              ])

