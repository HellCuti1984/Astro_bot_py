import asyncio

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from core import AstroApi, CitiesCheck
from core.pagination import pagi_config

from handlers.start_handler import start_message

from keyboards import menu
from keyboards.cities import get_pagi_cities_markup
from keyboards.ports import get_pagi_ports_markup
from keyboards.priority_city_check import pr_city_keyboard


async def get_balance(call: CallbackQuery):
    await call.answer(text=f"{AstroApi.get_balance()}", show_alert=True)


async def get_cities(call: CallbackQuery):
    await call.answer(cache_time=5)

    keyboard = get_pagi_cities_markup()

    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


async def priority_cities(call: CallbackQuery):
    await call.answer(cache_time=5)
    keyboard = pr_city_keyboard()
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


async def get_ports(call: CallbackQuery):
    await call.answer(cache_time=5)
    pagi_config.TEXT = 'Список портов:'
    pagi_config.INLINE_BUTTONS = []
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=get_pagi_ports_markup(from_file=True, by_city=True))


async def refresh_ports(call: CallbackQuery):
    await call.answer(cache_time=5)

    try:
        AstroApi.update_port_file()

        await call.answer(text=f"Список успешно обновлен")
    except ValueError:
        await call.answer(text=f"Ошибка обновления списка")


async def open_pr_cities_list(call: CallbackQuery):
    await call.answer(cache_time=5)
    CitiesCheck.IS_CHECKING_BY_TIMER = False
    keyboard = pr_city_keyboard()
    await call.message.edit_text(text=pagi_config.TEXT, reply_markup=keyboard)


async def renew_archived(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text='ЗАПУСК ОБНОВЛЕНИЯ АРХИВА...')
    await asyncio.sleep(1)

    updated_count = 0
    archived_ports = AstroApi.get_archived_ports()
    for port in archived_ports:

        await call.message.edit_text(text=f"ОБНОВЛЕНИЕ ПОРТА --- {port['name']} / {port['id']}")
        status = AstroApi.post_renew_port(port['id'])
        updated_count += 1
        await asyncio.sleep(0.5)
        if status['status'] != 'ok':
            await call.message.answer(
                text=f'ОШИБКА ОБНОВЛЕНИЯ. ПРОВЕРЬТЕ БАЛАНС\nОбновлено: {updated_count} / Осталось в архиве {len(AstroApi.get_archived_ports())} шт.')
            await call.message.edit_text(text=f"{start_message()}", reply_markup=menu.menu_markup())
            return

    await call.message.answer(text='ВСЕ ПОРТЫ ОБНОВЛЕНЫ')
    await call.message.edit_text(text=f"{start_message()}", reply_markup=menu.menu_markup())


async def back_to_menu(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.edit_text(text=f"{start_message()}", reply_markup=menu.menu_markup())


def register_menu_handler(dp: Dispatcher):
    dp.register_callback_query_handler(get_balance, text='get_balance')
    dp.register_callback_query_handler(get_cities, text='get_cities')
    dp.register_callback_query_handler(get_ports, text='get_ports')
    dp.register_callback_query_handler(refresh_ports, text='refresh_ports')
    dp.register_callback_query_handler(renew_archived, text='renew_archived')
    dp.register_callback_query_handler(open_pr_cities_list, text='priority_cities')
    dp.register_callback_query_handler(back_to_menu, text='back_to_menu')
