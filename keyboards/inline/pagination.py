from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core import AstroApi
from handlers.users import pagination


def pagination_row(markup, paginator=1, max_pages=1):
    pagination_button = {
        'goto_first': InlineKeyboardButton(text="\u00AB", callback_data="go_to_first_page"),
        'goto_next': InlineKeyboardButton(text=f"\u2039", callback_data='prev_slide_page'),
        'goto_curr': InlineKeyboardButton(text=f"\u2022 {paginator} \u2022", callback_data='cur_slide_page'),
        'goto_prev': InlineKeyboardButton(text=f"\u203A", callback_data='new_slide_page'),
        'goto_last': InlineKeyboardButton(text=f"\u00BB", callback_data='go_to_last_page')
    }

    if paginator > 1:
        markup.row(
            pagination_button['goto_first'],
            pagination_button['goto_next'],
            pagination_button['goto_curr'],
            pagination_button['goto_prev'],
            pagination_button['goto_last']
        )
    elif paginator == 1:
        markup.row(
            pagination_button['goto_curr'],
            pagination_button['goto_prev'],
            pagination_button['goto_last']
        )
    elif paginator is max_pages:
        markup.row(
            pagination_button['goto_first'],
            pagination_button['goto_next'],
            pagination_button['goto_curr']
        )

    return markup
