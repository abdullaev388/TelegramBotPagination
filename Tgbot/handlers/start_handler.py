from aiogram import Dispatcher
from aiogram.types import Message


async def start_handler(message: Message):
    ...


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands='start')
