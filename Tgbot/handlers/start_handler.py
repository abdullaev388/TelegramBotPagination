from aiogram import Dispatcher
from aiogram.types import Message

from Tgbot import config
from Tgbot.keyboards.pagination import pagination_keyboard


async def start_handler(message: Message):
    current_index = 0
    caption = "%d/%d" % (current_index + 1, config.max_index + 1)

    with open(config.PHOTOS[current_index], mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=caption,
                                   reply_markup=pagination_keyboard(index=current_index))


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands='start')
