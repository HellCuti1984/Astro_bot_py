from aiogram import Dispatcher, types

from core import AstroApi
import config
from keyboards import menu


def start_message():
    calc = AstroApi.get_calculate()
    port_cost = calc['port_cost']
    traffic_cost = calc['traffic_cost'] + port_cost
    port_and_traffic = calc['port_and_traffic']

    return "Цены: \n" \
           f"     \u2022 Порт: {port_cost} руб.\n" \
           f"     \u2022 Трафик (100 Мб): {round(traffic_cost - port_cost, 2)} руб.\n" \
           f"     \u2022 Порт+трафик: {port_and_traffic} руб.\n"


async def bot_start(message: types.Message):
    is_admin = False
    user_id = f'{message.from_user.id}'
    for admin in config.ADMINS:
        if user_id == admin:
            await message.answer(start_message(), reply_markup=menu.menu_markup())
            return
        else:
            is_admin = False

    if is_admin is False:
        await message.answer('О боже! Ты не админ! Пошел нах#й отсюда!...\n\n\n\nhe-he')
        return


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start')
