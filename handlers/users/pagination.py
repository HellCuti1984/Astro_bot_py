from aiogram.types import CallbackQuery

from loader import dp
from jsons import paginations
from keyboards.inline import markups

content = []


@dp.callback_query_handler(text='go_to_first_page')
async def go_to_first_page(call: CallbackQuery):
    pass


@dp.callback_query_handler(text='prev_slide_page')
async def prev_slide_page(call: CallbackQuery):
    pass


@dp.callback_query_handler(text='cur_slide_page')
async def cur_slide_page(call: CallbackQuery):
    await call.answer('Список городов', show_alert=True)


@dp.callback_query_handler(text='new_slide_page')
async def new_slide_page(call: CallbackQuery):
    pass


@dp.callback_query_handler(text='go_to_last_page')
async def go_to_last_page(call: CallbackQuery):
    pass
