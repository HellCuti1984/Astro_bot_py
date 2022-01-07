from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.Archive import status


def menu_markup():
    # Создание клавиатуры
    markup_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Баланс', callback_data='get_balance')
            ],
            [
                InlineKeyboardButton(text='Города', callback_data='get_cities')
            ],
            [
                InlineKeyboardButton(text='Список портов', callback_data='get_ports'),
                InlineKeyboardButton(text='Обновить порты  \u21ba', callback_data='refresh_ports'),
            ],
            [
                InlineKeyboardButton(text='Список приор. город', callback_data='priority_cities'),
                InlineKeyboardButton(text='Добавить город', callback_data='add_priority_cities')
            ],
            [
                InlineKeyboardButton(text=status, callback_data='renew_archived')
            ]
        ]
    )

    return markup_inline
