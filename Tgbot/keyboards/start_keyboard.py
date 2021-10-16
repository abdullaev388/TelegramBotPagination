from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choose_pagination_type():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='pagination 1',
                    callback_data='pg1'
                ),
                InlineKeyboardButton(
                    text='pagination 2',
                    callback_data='pg2'
                )
            ]
        ]
    )