from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core import jsons, AstroApi
from core.pagination import pagi_config

from handlers.cities_handler import city_callback
from keyboards.pagination import pagination_keyboard


def get_pagi_cities_markup(from_from_file=False):
    if from_from_file is False:
        cities = AstroApi.get_cities_from_api()
    else:
        cities = AstroApi.get_cities_from_file()

    pagi_config.TEXT = 'Список городов:'
    pagi_config.CALLBACK_DATA = 'open_city'
    pagi_config.CONTENT = cities
    pagi_config.IS_BACK_MENU_BTN = True

    pagi_config.INLINE_BUTTONS.clear()
    for city in cities:
        city_btn = InlineKeyboardButton(text=str(city['name']), callback_data=pagi_config.CALLBACK_DATA)
        buy_port = InlineKeyboardButton(text='\u0024', callback_data=city_callback.new(
            lot_name=str(city['name']), count=1
        ))

        pagi_config.INLINE_BUTTONS.append([city_btn, buy_port])

    return pagination_keyboard()
