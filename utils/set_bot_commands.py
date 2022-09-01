from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("test", "Тест"),
        types.BotCommand("form", "Форма"),
        types.BotCommand("menu", "Меню"),
    ])
