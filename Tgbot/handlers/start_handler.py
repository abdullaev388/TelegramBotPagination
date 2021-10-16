from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from Tgbot import config
from Tgbot.keyboards.pagination import pagination_keyboard, pagination_2_keyboard
from Tgbot.keyboards.start_keyboard import choose_pagination_type


async def start_handler(message: Message):
    await message.answer('Choose type of pagination', reply_markup=choose_pagination_type())


async def choose_pagination(call: CallbackQuery):
    pg_type = call.data
    current_index = 0

    if pg_type == 'pg1':
        keyboard = pagination_keyboard(index=current_index)
        caption = "%d/%d" % (current_index + 1, config.max_index + 1)
    else:
        keyboard = pagination_2_keyboard(index=current_index)
        caption = None

    await call.message.delete()
    with open(config.PHOTOS[current_index], mode='rb') as photo:
        await call.message.answer_photo(photo=photo, caption=caption,
                                        reply_markup=keyboard)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands='start')
    dp.register_callback_query_handler(choose_pagination, text=['pg1', 'pg2'])
