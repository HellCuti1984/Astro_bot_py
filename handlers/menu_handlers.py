import requests
from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from core import AstroApi, jsons, market
from core.market import market
from core.pagination import pagi_config

from handlers.start_handler import start_message

from keyboards import menu, ports
from keyboards.cities import get_pagi_cities_markup
from keyboards.ports import get_pagi_ports_markup


async def get_balance(call: CallbackQuery):
    await call.answer(text=f"{AstroApi.get_balance()}", show_alert=True)


async def get_cities(call: CallbackQuery):
    await call.answer(cache_time=5)

    keyboard = get_pagi_cities_markup()

    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


async def priority_cities(call: CallbackQuery):
    await call.answer(cache_time=15)
    keyboard = get_pagi_cities_markup()
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


async def add_priority_cities(call: CallbackQuery):
    pass


async def get_ports(call: CallbackQuery):
    await call.answer(cache_time=15)
    pagi_config.TEXT = 'Список портов:'
    pagi_config.INLINE_BUTTONS = []
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=get_pagi_ports_markup(from_file=True, by_city=True))


async def refresh_ports(call: CallbackQuery):
    await call.answer(cache_time=20)

    try:
        path_to_priority_cities_file = jsons.FILES['path_to_ports_file']
        cities = AstroApi.get_ports_from_api()
        jsons.write_to_file(cities, path_to_priority_cities_file)

        await call.answer(text=f"Список успешно обновлен")
    except ValueError:
        await call.answer(text=f"Ошибка обновления списка")


async def back_to_menu(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text=f"{start_message()}", reply_markup=menu.menu_markup())


async def FOR_TESTS(call: CallbackQuery):
    await call.answer(cache_time=5)

    ports_list = AstroApi.get_ports_from_file()
    ports.get_ports_by_city(ports_list)

    await call.answer(text='Готово, хули', show_alert=True)


def register_menu_handler(dp: Dispatcher):
    dp.register_callback_query_handler(get_balance, text='get_balance')
    dp.register_callback_query_handler(get_cities, text='get_cities')
    dp.register_callback_query_handler(get_ports, text='get_ports')
    dp.register_callback_query_handler(priority_cities, text='priority_cities')
    dp.register_callback_query_handler(add_priority_cities, text='add_priority_cities')
    dp.register_callback_query_handler(refresh_ports, text='refresh_ports')
    dp.register_callback_query_handler(back_to_menu, text='back_to_menu')
    dp.register_callback_query_handler(FOR_TESTS, text='FOR_TESTS')
