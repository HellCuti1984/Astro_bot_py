from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData

from core import jsons
from core.pagination import pagi_config
from keyboards import ports

ports_list_by_city = CallbackData('ports_list', 'ports_list_by_city')
get_port_info = CallbackData('port_info', 'id_port')


async def get_ports_list_by_city(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    city = callback_data.get('ports_list_by_city')

    keyboard = ports.get_pagi_ports_by_city_markup(city)

    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


async def get_port_inf(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    port_path = jsons.FILES['path_to_ports_file']
    port = jsons.get_by_attribute_value(path=port_path, attr='id', val=int(callback_data.get('id_port')))

    keyboard = ports.get_port_info_by_id_markup()
    await call.message.edit_text(text=f'{port}', reply_markup=keyboard)


def register_ports_handler(dp: Dispatcher):
    dp.register_callback_query_handler(get_ports_list_by_city, ports_list_by_city.filter())
    dp.register_callback_query_handler(get_port_inf, get_port_info.filter())
