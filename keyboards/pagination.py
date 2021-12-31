from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from core.jsons import get_like_pages
from core.pagination import pagi_config
from keyboards.buttons import add_back_menu_btn

pagination_callback = CallbackData('pagination', 'current_index')


def get_prev_next_index(index):
    if index == pagi_config.MIN_INDEX:
        previous_index = index
    else:
        previous_index = index - 1

    if index == pagi_config.MAX_INDEX:
        next_index = index
    else:
        next_index = index + 1

    return previous_index, next_index


def get_prev_next_buttons(previous_index, next_index, callback_factory):
    return [
        InlineKeyboardButton(
            text='⬅',
            callback_data=callback_factory.new(current_index=previous_index)
        ),
        InlineKeyboardButton(
            text='➡',
            callback_data=callback_factory.new(current_index=next_index)
        )
    ]


def pagination_keyboard(index=0):
    previous_buttons = [
        InlineKeyboardButton(
            text=f"{i + 1}",
            callback_data=pagination_callback.new(current_index=i)
        )
        for i in range(index - 2, index)
        if 0 <= i <= len(pagi_config.CONTENT)
    ]

    previous_buttons.append(InlineKeyboardButton(
        text=f'|{index + 1}|',
        callback_data='current'
    ))

    next_buttons = [
        InlineKeyboardButton(
            text=f"{i + 1}",
            callback_data=pagination_callback.new(current_index=i)
        )
        for i in range(index + 1, index + 3)
        if i <= len(pagi_config.CONTENT)
    ]

    keyboard = InlineKeyboardMarkup(row_width=5)

    if len(pagi_config.INLINE_BUTTONS) == 0:
        page_of_content = get_like_pages(pagi_config.CONTENT, index)
        for cont in page_of_content:
            keyboard.row(InlineKeyboardButton(text=str(cont['name']), callback_data=pagi_config.CALLBACK_DATA))
    else:
        page_of_content = get_like_pages(pagi_config.INLINE_BUTTONS, index)
        for btn in page_of_content:
            keyboard.add(*btn)

    buttons = previous_buttons + next_buttons
    keyboard.add(*buttons)

    previous_index, next_index = get_prev_next_index(index)
    buttons = get_prev_next_buttons(previous_index=previous_index, next_index=next_index,
                                    callback_factory=pagination_callback)
    keyboard.add(*buttons)

    if pagi_config.CUSTOM_BUTTON is not None:
        keyboard.add(pagi_config.CUSTOM_BUTTON)

    # ДОБАВИТЬ ВОЗВРАТ МЕНЮ
    if pagi_config.IS_BACK_MENU_BTN is True:
        keyboard = add_back_menu_btn(keyboard)

    return keyboard
