import time

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData

from core import jsons
from core import AstroApi
from core.pagination import pagi_config
from keyboards import ports

ports_list_by_city = CallbackData('ports_list', 'ports_list_by_city')
get_port_info = CallbackData('port_info', 'id_port')
post_renew_port = CallbackData('renew_port', 'id_port')
delete_port = CallbackData('delete_port', 'id_port')


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

    text = f"ИНФОРМАЦИЯ ПРО ПОРТ --- {port['name']}" \
           f"\n\n Имя: {port['name']}" \
           f"\n Адрес: {port['node']['ip']}:{port['ports']['http']}" \
           f"\n Город: {port['city']}" \
           f"\n Группа: {port['group']}" \
           f"\n Данные для входа: {port['access']['login']} / {port['access']['password']}" \
           f"\n\n Траффик: Всего - {port['traffic']['total_mb']} MB / Использовано - {port['traffic']['used_mb']} MB / Осталось - {port['traffic']['left_mb']} MB"

    keyboard = ports.get_port_info_by_id_markup(port)
    await call.message.edit_text(text=f'{text}', reply_markup=keyboard)


async def renew_port(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    status = AstroApi.post_renew_port(int(callback_data.get('id_port')))

    await call.message.edit_text(text=f'ОБНОВЛЕНИЕ ПОРТА ...')
    time.sleep(2)

    if status['status'] == 'ok':
        await call.message.edit_text(text=f'ПОРТ УСПЕШНО ОБНОВЛЕН!')
    else:
        await call.message.edit_text(text=f"ОШИБКА ОБНОВЛЕНИЯ --- Недостаточно средств")
    time.sleep(2)

    # ВОЗВРАТ К СПИСКУ ПОРТОВ
    AstroApi.update_port_file()
    keyboard = ports.get_pagi_ports_markup(from_file=True, by_city=True)
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


async def del_port(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    status = AstroApi.delete_port(int(callback_data.get('id_port')))

    await call.message.edit_text(text=f'УДАЛЕНИЕ ПОРТА ...')
    time.sleep(2)
    if status['status'] == 'ok':
        await call.message.edit_text(text=f'ПОРТ УСПЕШНО УДАЛЕН!')
    else:
        await call.message.edit_text(text=f"ОШИБКА УДАЛЕНИЯ --- {status['errors']}")
    time.sleep(2)

    # ВОЗВРАТ К СПИСКУ ПОРТОВ
    AstroApi.update_port_file()
    keyboard = ports.get_pagi_ports_markup(from_file=True, by_city=True)
    await call.message.edit_text(text=pagi_config.TEXT,
                                 reply_markup=keyboard)


def register_ports_handler(dp: Dispatcher):
    dp.register_callback_query_handler(get_ports_list_by_city, ports_list_by_city.filter())
    dp.register_callback_query_handler(get_port_inf, get_port_info.filter())
    dp.register_callback_query_handler(renew_port, post_renew_port.filter())
    dp.register_callback_query_handler(del_port, delete_port.filter())
