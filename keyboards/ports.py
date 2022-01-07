from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core import AstroApi
from core.pagination import pagi_config
from handlers.ports_handler import ports_list_by_city, get_port_info, post_renew_port, delete_port

from keyboards.pagination import pagination_keyboard


def get_pagi_ports_markup(from_file=False, by_city=False):
    if from_file is False:
        ports = AstroApi.get_ports_from_api()
    else:
        ports = AstroApi.get_ports_from_file()

    def get_ports_by_city(port_list):
        city_list = []
        city_list_out = []

        for port in port_list:
            city_list.append(port['city'])

        city_list = list(dict.fromkeys(city_list))

        for city in city_list:
            city_list_out.append({'name': city})

        return city_list_out

    if by_city is True:
        ports = get_ports_by_city(ports)

    pagi_config.TEXT = 'Список портов:'
    pagi_config.CALLBACK_DATA = 'ports_list'
    pagi_config.CONTENT = ports
    pagi_config.IS_BACK_MENU_BTN = True

    pagi_config.INLINE_BUTTONS.clear()
    for port in ports:
        port_btn = InlineKeyboardButton(text=str(port['name']),
                                        callback_data=ports_list_by_city.new(ports_list_by_city=port['name']))
        pagi_config.INLINE_BUTTONS.append([port_btn])

    return pagination_keyboard()


def get_pagi_ports_by_city_markup(city):
    ports_list_content = AstroApi.get_ports_from_file()

    pagi_config.TEXT = f'Порты {city}:'
    pagi_config.CALLBACK_DATA = 'open_city'
    pagi_config.CONTENT = ports_list_content
    pagi_config.IS_BACK_MENU_BTN = False

    pagi_config.INLINE_BUTTONS.clear()
    for port in ports_list_content:
        if port['city'] == city:
            port_info_btn = InlineKeyboardButton(text=port['name'], callback_data=get_port_info.new(
                id_port=port['id']
            ))

            pagi_config.INLINE_BUTTONS.append([port_info_btn])

    return pagination_keyboard()


def get_port_info_by_id_markup(port):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Продлить', callback_data=post_renew_port.new(id_port=port['id'])),
                InlineKeyboardButton(text='Удалить', callback_data=delete_port.new(id_port=port['id']))
            ],
            [
                InlineKeyboardButton(text='К портам', callback_data='get_ports')
            ],
            [
                InlineKeyboardButton(text='В меню', callback_data='back_to_menu')
            ]
        ]
    )

    return keyboard
