from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.market import market


def get_buy_port_markup():
    markup_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Купить', callback_data='final_buy_port')
            ],
            [
                InlineKeyboardButton(text='-', callback_data='minus_traffic_port'),
                InlineKeyboardButton(text=f'{round(market.TRAFFIC*1000)}', callback_data='cur_traffic_port'),
                InlineKeyboardButton(text='+', callback_data='plus_traffic_port')
            ],
            [
                InlineKeyboardButton(text='-', callback_data='minus_count_port'),
                InlineKeyboardButton(text=f'{market.COUNT}', callback_data='cur_count_port'),
                InlineKeyboardButton(text='+', callback_data='plus_count_port')
            ],
            [
                InlineKeyboardButton(text='Отмена', callback_data='get_cities')
            ]
        ]
    )

    return markup_inline
