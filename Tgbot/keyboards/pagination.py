from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from Tgbot import config

pagination_callback = CallbackData('pagination', 'current_index')


def pagination_keyboard(index):
    if index == config.min_index:
        previous_index = index
    else:
        previous_index = index - 1

    if index == config.max_index:
        next_index = index
    else:
        next_index = index + 1

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='⬅',
                    callback_data=pagination_callback.new(current_index=previous_index)
                ),
                InlineKeyboardButton(
                    text='➡',
                    callback_data=pagination_callback.new(current_index=next_index)
                )
            ]
        ]
    )
