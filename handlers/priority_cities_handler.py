import asyncio

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from core import CitiesCheck, AstroApi, jsons
from handlers.cities_handler import city_callback

pr_cities_list = CallbackData('pr_cities_list', 'city_name')


async def pr_city_control(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    city = callback_data.get('city_name')
    CitiesCheck.add_remove_pr_cities(city)


async def start_cities_check(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text='ЗАПУСК ОТСЛЕЖИВАНИЯ ГОРОДОВ ....')
    await asyncio.sleep(1)

    CitiesCheck.IS_CHECKING_BY_TIMER = True

    while CitiesCheck.IS_CHECKING_BY_TIMER:
        cities = AstroApi.get_cities_from_api()
        pr_cities = jsons.read_from_file(CitiesCheck.path_to_priority_cities_file)

        for pr_city in pr_cities:
            for city in cities:
                if city['name'] == pr_city['name']:
                    keyboard = InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text='Купить',
                                                     callback_data=city_callback.new(lot_name=str(city['name']),
                                                                                     count=1))
                            ]
                        ])

                    await call.message.answer(text=f"Город {pr_city['name']} доступен для покупки",
                                              reply_markup=keyboard)

        await asyncio.sleep(900)


def register_pr_cities_handler(dp: Dispatcher):
    dp.register_callback_query_handler(pr_city_control, pr_cities_list.filter())
    dp.register_callback_query_handler(start_cities_check, text='start_cities_check')
