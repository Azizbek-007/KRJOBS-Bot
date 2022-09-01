from aiogram.dispatcher.filters.state import StatesGroup, State


class Resume(StatesGroup):
    fullname = State()
    brithday = State()
    can = State()
    experience = State()
    telegram = State()
    contact = State()
    live = State()
    salary = State()
    goal = State()
