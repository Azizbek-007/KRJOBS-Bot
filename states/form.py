from aiogram.dispatcher.filters.state import StatesGroup, State

class Vacancy(StatesGroup):
    Level = State()
    Company = State()
    Job = State()
    Required = State()
    Benefits = State()
    Salary = State()
    Contact = State()
