from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from Tgbot import config

pagination_callback = CallbackData('pagination', 'current_index')
pagination_2_callback = CallbackData('pagination2', 'current_index')


def get_prev_next_index(index):
    if index == config.min_index:
        previous_index = index
    else:
        previous_index = index - 1

    if index == config.max_index:
        next_index = index
    else:
        next_index = index + 1

    return previous_index, next_index


def get_prev_next_buttons(previous_index, next_index, callback_factory):
    return [
        InlineKeyboardButton(
            text='⬅',
            callback_data=callback_factory.new(current_index=previous_index)
        ),
        InlineKeyboardButton(
            text='➡',
            callback_data=callback_factory.new(current_index=next_index)
        )
    ]


def pagination_keyboard(index):
    previous_index, next_index = get_prev_next_index(index)
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = get_prev_next_buttons(previous_index=previous_index, next_index=next_index,
                                    callback_factory=pagination_callback)
    keyboard.add(*buttons)
    return keyboard


def pagination_2_keyboard(index):
    previous_buttons = [
        InlineKeyboardButton(
            text=f"{i + 1}",
            callback_data=pagination_2_callback.new(current_index=i)
        )
        for i in range(index - 2, index)
        if 0 <= i <= len(config.PHOTOS)
    ]
    previous_buttons.append(InlineKeyboardButton(
        text=f'|{index + 1}|',
        callback_data='current'
    ))
    next_buttons = [
        InlineKeyboardButton(
            text=f"{i + 1}",
            callback_data=pagination_2_callback.new(current_index=i)
        )
        for i in range(index + 1, index + 3)
        if i < len(config.PHOTOS)
    ]

    buttons = previous_buttons + next_buttons
    keyboard = InlineKeyboardMarkup(row_width=5)
    keyboard.add(*buttons)

    previous_index, next_index = get_prev_next_index(index)
    buttons = get_prev_next_buttons(previous_index=previous_index, next_index=next_index,
                                    callback_factory=pagination_2_callback)
    keyboard.add(*buttons)

    return keyboard
