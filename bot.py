import os
import telebot
from telebot import types
import AstroApi
import markups
from settings import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


def menu_markup():
    # Создание клавиатуры
    markup_inline = types.InlineKeyboardMarkup(row_width=3)
    # Создание клавиш
    item_get_balance = types.InlineKeyboardButton(text='Баланс', callback_data='get_balance')
    item_get_calculate = types.InlineKeyboardButton(text='Расчет стоимости порта', callback_data='get_calculate')
    item_get_cities = types.InlineKeyboardButton(text='Список городов', callback_data='get_cities')
    item_buy_ports = types.InlineKeyboardButton(text='Покупка портов', callback_data='buy_ports')

    markup_inline.row(item_get_balance, item_get_cities)
    markup_inline.row(item_get_calculate)
    markup_inline.row(item_buy_ports)

    return markup_inline


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "get_balance":
        # bot.answer_callback_query(call.id, AstroApi.get_balance())
        bot.answer_callback_query(callback_query_id=call.id, text=AstroApi.get_balance())
    elif call.data == "get_calculate":
        bot.answer_callback_query(call.id, "Расчет стоимости пока не актвен")
    elif call.data == "get_cities":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              reply_markup=markups.cities_markup(),
                              text='Список городов!')
    elif call.data == "back_to_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=menu_markup(),
                              text='Приветствую. Выбери необходимую информацию')

    bot.answer_callback_query(callback_query_id=call.id)


@bot.message_handler(commands=['start'])
def message_handler(message):
    bot.send_message(message.chat.id, "Приветствую. Выбери необходимую информацию", reply_markup=menu_markup())


bot.polling(none_stop=True, interval=0)
