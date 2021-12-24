from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from core import AstroApi
from data import config
from loader import dp

from keyboards.inline.markups import menu_markup


def start_message():
    port_cost = 15
    traffic_cost = AstroApi.get_calculate(city='Moscow', volume=100, count=1)['cost']
    port_and_traffic = port_cost + traffic_cost - port_cost

    return "Приветствую. \n\n" \
           "Цены: \n" \
           f"     \u2022 Порт: {port_cost} руб.\n" \
           f"     \u2022 Трафик (100 Мб): {round(traffic_cost - port_cost, 2)} руб.\n" \
           f"     \u2022 Порт+трафик: {port_and_traffic} руб.\n"


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    is_admin = False
    user_id = f'{message.from_user.id}'
    for admin in config.ADMINS:
        if user_id == admin:
            await message.answer(start_message(), reply_markup=menu_markup)
            return
        else:
            is_admin = False

    if is_admin is False:
        await message.answer('О боже! Ты не админ! Пошел нахуй отсюда!...\n\n\n\nhe-he')
        return
