import os

from aiogram.types import InlineKeyboardButton

from core import jsons
from core.CitiesCheck import check_city_in_priority_list
from core.pagination import pagi_config
from handlers.priority_cities_handler import pr_cities_list
from keyboards.pagination import pagination_keyboard

path_to_priority_cities_file = os.getcwd() + "\\data\\priority_cities.json"
path_to_all_cities_list = os.getcwd() + "\\data\\all_priority_cities.json"


def pr_city_keyboard():
    cities_list = jsons.read_from_file(path_to_all_cities_list)

    pagi_config.TEXT = f'Список всех городов:'
    pagi_config.CALLBACK_DATA = 'add_to_priority_cities_list_file'
    pagi_config.CONTENT = cities_list
    pagi_config.IS_BACK_MENU_BTN = True
    pagi_config.CUSTOM_BUTTON = None
    pagi_config.INLINE_BUTTONS.clear()

    X_emoji = '\U0000274c'
    PLUS_emoji = '\U00002714'

    for city in cities_list:
        if check_city_in_priority_list(city['name']):
            city_btn = InlineKeyboardButton(text=f"{city['name']} {PLUS_emoji}", callback_data=pr_cities_list.new(
                city_name=city['name']
            ))
        else:
            city_btn = InlineKeyboardButton(text=f"{city['name']} {X_emoji}", callback_data=pr_cities_list.new(
                city_name=city['name']
            ))

        pagi_config.INLINE_BUTTONS.append([city_btn])
    return pagination_keyboard()
