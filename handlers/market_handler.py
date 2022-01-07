import time

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from core import AstroApi
from core.AstroApi import post_create_port
from core.market import market
from core.pagination import pagi_config
from keyboards.cities import get_pagi_cities_markup
from keyboards.market import get_buy_port_markup

traffic_count = [0.1, 0.3, 0.5, 1]


def get_traffic_port_price():
    calc = AstroApi.get_calculate()
    price = int(traffic_count[market.TRAFFIC_INDEX] * 10) * int(market.COUNT) * calc['traffic_cost']
    return round(price, 2)


def buy_port_message():
    return f'Купить порт: {market.LOT_NAME}\nЦена: {get_traffic_port_price()}'


async def plus_traffic_port(call: CallbackQuery):
    await call.answer(cache_time=1)
    market.TRAFFIC_INDEX += 1

    if market.TRAFFIC_INDEX == 1:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]
    elif market.TRAFFIC_INDEX == 2:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]
    elif market.TRAFFIC_INDEX == 3:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]
    elif market.TRAFFIC_INDEX == 4:
        market.TRAFFIC_INDEX -= 1
        return

    await call.message.edit_text(text=buy_port_message(),
                                 reply_markup=get_buy_port_markup())


async def minus_traffic_port(call: CallbackQuery):
    await call.answer(cache_time=1)
    market.TRAFFIC_INDEX -= 1

    if market.TRAFFIC_INDEX < 0:
        market.TRAFFIC_INDEX = 0
    elif market.TRAFFIC_INDEX == 0:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]
    elif market.TRAFFIC_INDEX == 3:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]
    elif market.TRAFFIC_INDEX == 2:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]
    elif market.TRAFFIC_INDEX == 1:
        market.TRAFFIC = traffic_count[market.TRAFFIC_INDEX]

    await call.message.edit_text(text=buy_port_message(), reply_markup=get_buy_port_markup())


async def minus_count_port(call: CallbackQuery):
    await call.answer(cache_time=1)
    if market.COUNT != 0:
        market.COUNT = int(market.COUNT) - 1
    else:
        return

    await call.message.edit_text(text=buy_port_message(), reply_markup=get_buy_port_markup())


async def plus_count_port(call: CallbackQuery):
    await call.answer(cache_time=1)
    market.COUNT = int(market.COUNT) + 1
    await call.message.edit_text(text=buy_port_message(), reply_markup=get_buy_port_markup())


async def final_buy_port(call: CallbackQuery):
    await call.answer(cache_time=5)

    await call.message.edit_text(text=f'ОЖИДАЙТЕ. ПОКУПКА {market.COUNT} ПОРТОВ...')

    # ПОКУПКА ПОРТА. ВО ВРЕМЯ ТЕСТИРОВАНИЯ ЛУЧШЕ НАХУЙ В КОММЕНТАРИЙ ОТПРАВИТЬ
    status = post_create_port(name=market.LOT_NAME,
                              city=market.LOT_NAME,
                              volume=traffic_count[market.TRAFFIC_INDEX])

    if status is True:
        await call.message.answer(text=f'Порт: {market.LOT_NAME} успешно куплен.\nЦена: {get_traffic_port_price()}')
    else:
        await call.message.answer(text=f'ОШИБКА ПОКУПКИ. НЕДОСТАТОЧНО СРЕДСТВ')

    time.sleep(2)
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=get_pagi_cities_markup())


def register_market_handler(dp: Dispatcher):
    dp.register_callback_query_handler(final_buy_port, text='final_buy_port')
    dp.register_callback_query_handler(minus_traffic_port, text='minus_traffic_port')
    dp.register_callback_query_handler(plus_traffic_port, text='plus_traffic_port')
    dp.register_callback_query_handler(minus_count_port, text='minus_count_port')
    dp.register_callback_query_handler(plus_count_port, text='plus_count_port')
