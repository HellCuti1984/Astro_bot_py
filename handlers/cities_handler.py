from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData

from core import AstroApi
from core.market import market
from keyboards.market import get_buy_port_markup

city_callback = CallbackData('buy_port', 'lot_name', 'count')


async def open_city(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)

    market.LOT_NAME = callback_data.get('lot_name')
    market.COUNT = callback_data.get('count')

    calc = AstroApi.get_calculate()
    price = int(0.1 * 10) * int(market.COUNT) * calc['traffic_cost']

    await call.message.edit_text(text=f'Купить порт: {market.LOT_NAME}\nЦена: {round(price, 2)}',
                                 reply_markup=get_buy_port_markup())


def register_cities_handler(dp: Dispatcher):
    dp.register_callback_query_handler(open_city, city_callback.filter())
