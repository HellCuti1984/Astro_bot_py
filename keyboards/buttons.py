from aiogram.types import InlineKeyboardButton


def add_back_menu_btn(keyboard):
    back_btn = [
        InlineKeyboardButton(
            text='В меню',
            callback_data='back_to_menu'
        )
    ]
    keyboard.add(*back_btn)

    return keyboard
