from telebot import types

import AstroApi


def cities_markup():
    cities = AstroApi.get_cities()
    cities_count = len(cities)
    city_pages_count = round(cities_count / 5)

    markup_inline = types.InlineKeyboardMarkup(row_width=cities_count + 1)

    iterator = 0
    for city in cities:
        item_get_balance = types.InlineKeyboardButton(text=str(city['name']), callback_data=f"city_{iterator + 1}")
        markup_inline.row(item_get_balance)

    item_first_btn_page = types.InlineKeyboardButton(text="\u00AB", callback_data="go_to_first_page")
    item_prev_btn_page = types.InlineKeyboardButton(text=f"\u2039", callback_data='prev_slide_page')
    item_cur_btn_page = types.InlineKeyboardButton(text=f"*{2}*", callback_data='cur_slide_page')
    item_next_btn_page = types.InlineKeyboardButton(text=f"\u203A", callback_data='new_slide_page')
    item_last_btn_page = types.InlineKeyboardButton(text=f"\u00BB", callback_data='go_to_last_page')
    markup_inline.row(item_first_btn_page, item_prev_btn_page, item_cur_btn_page, item_next_btn_page,
                      item_last_btn_page)
    # Кнопка возврата к меню
    item_get_balance = types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')
    markup_inline.row(item_get_balance)

    return markup_inline
