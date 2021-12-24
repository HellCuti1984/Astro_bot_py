from aiogram import types
from aiogram.contrib.middlewares import logging
from aiogram.types import CallbackQuery

from handlers.users.start import start_message
from jsons import jsons
from keyboards.inline import markups

from core import AstroApi
from loader import dp


@dp.callback_query_handler(text='back_to_menu')
async def back_to_menu(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text=f"{start_message()}", reply_markup=markups.menu_markup)


@dp.callback_query_handler(text='FOR_TESTS')
async def TESTS(call: CallbackQuery):
    data = AstroApi.get_cities_from_file()
    print(jsons.get_like_pages(data, limit=5))


@dp.callback_query_handler(text='get_balance')
async def get_balance(call: CallbackQuery):
    await call.answer(text=f"{AstroApi.get_balance()}", show_alert=True)


@dp.callback_query_handler(text='get_cities')
async def get_cities(call: CallbackQuery):
    await call.answer(cache_time=5)
    cities_from_api = AstroApi.get_cities_from_api()
    cities_markup = markups.cities_markup(cities_from_api, limit=10)
    await call.message.edit_text(text='Список городов:', reply_markup=cities_markup)


@dp.callback_query_handler(text='priority_cities')
async def priority_cities(call: CallbackQuery):
    await call.answer(cache_time=5)
    cities_from_api = AstroApi.get_cities_from_api()
    cities_markup = markups.cities_markup(cities_from_api)
    await call.message.edit_text(text='Список приор. городов:', reply_markup=cities_markup)


@dp.callback_query_handler(text='get_ports')
async def get_ports(call: CallbackQuery):
    await call.answer(cache_time=5)

    try:
        await call.message.edit_text(text='Список портов', reply_markup=markups.ports_markup)
    except ValueError:
        await call.answer(text='Ошибка вывода портов')


@dp.callback_query_handler(text='refresh_ports')
async def refresh_ports(call: CallbackQuery):
    await call.answer(cache_time=20)

    try:
        path_to_priority_cities_file = jsons.FILES['path_to_priority_cities_file']
        cities = AstroApi.get_cities_from_api()
        jsons.write_to_file(cities, path_to_priority_cities_file)

        await call.answer(text=f"Список успешно обновлен")
    except ValueError:
        await call.answer(text=f"Ошибка обновления списка")
