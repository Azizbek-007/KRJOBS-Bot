from aiogram import Dispatcher

from .private_chat import IsPrivate
from .is_group import IsGroup
from .admins import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    pass
