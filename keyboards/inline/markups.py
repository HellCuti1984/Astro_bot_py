from jsons import jsons
from core import AstroApi
from keyboards.inline import pagination

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def back_btn():
    return InlineKeyboardButton(text='<-- Назад', callback_data='back_to_menu')


def menu_markup():
    # Создание клавиатуры
    markup_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Баланс', callback_data='get_balance'),
                InlineKeyboardButton(text='Города', callback_data='get_cities')
            ],
            [
                InlineKeyboardButton(text='Список портов', callback_data='get_ports'),
                InlineKeyboardButton(text='Обновить порты  \u21ba', callback_data='refresh_ports'),
            ],
            [
                InlineKeyboardButton(text='Список приор. город', callback_data='priority_cities'),
            ],
            [
                InlineKeyboardButton(text='ТЕСТОВАЯ КНОПКА', callback_data='FOR_TESTS')
            ]
        ]
    )

    return markup_inline


def cities_markup(content, limit=5):
    cities = jsons.get_like_pages(content, limit=limit)
    count_of_pages = round(len(cities) / limit)
    markup_inline = InlineKeyboardMarkup()

    # Вывод списка городов
    for iterator, city in enumerate(cities, 1):
        item_get_balance = InlineKeyboardButton(text=str(city['name']), callback_data=f"{city['name']}")
        markup_inline.row(item_get_balance)

    markup_inline = pagination.pagination_row(markup_inline, )
    markup_inline.row(back_btn())

    return markup_inline


def ports_markup(from_file=False):
    # if from_file is False:
    #    ports = AstroApi.get_ports_from_api()
    # else:
    #    ports = AstroApi.get_ports_from_file()

    markup = InlineKeyboardMarkup()

    # for iterator, port in enumerate(ports['ports'], 1):
    #   port_btn = InlineKeyboardButton(text=str(port['name']), callback_data=f"{port['name']}")
    #  markup.row(port_btn)

    markup.row(back_btn())

    return markup


menu_markup = menu_markup()
ports_markup = ports_markup()
