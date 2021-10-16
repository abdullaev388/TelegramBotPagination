from aiogram import Dispatcher
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.utils.exceptions import MessageNotModified

from Tgbot import config
from Tgbot.keyboards.pagination import pagination_keyboard, pagination_callback, pagination_2_keyboard, \
    pagination_2_callback


async def pagination(call: CallbackQuery, callback_data: dict):
    current_index = int(callback_data.get('current_index'))
    caption = "%d/%d" % (current_index + 1, config.max_index + 1)

    with open(config.PHOTOS[current_index], 'rb') as photo:
        media = InputMediaPhoto(media=photo, caption=caption)

        await call.answer()
        try:
            await call.message.edit_media(media=media,
                                          reply_markup=pagination_keyboard(current_index))
        except MessageNotModified:
            return


async def pagination2(call: CallbackQuery, callback_data: dict):
    current_index = int(callback_data.get('current_index'))

    with open(config.PHOTOS[current_index], 'rb') as photo:
        media = InputMediaPhoto(media=photo)

        await call.answer()
        try:
            await call.message.edit_media(media=media,
                                          reply_markup=pagination_2_keyboard(current_index))
        except MessageNotModified:
            return


def register_pagination_handler(dp: Dispatcher):
    dp.register_callback_query_handler(pagination, pagination_callback.filter())
    dp.register_callback_query_handler(pagination2, pagination_2_callback.filter())
