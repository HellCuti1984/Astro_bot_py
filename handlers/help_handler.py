from aiogram import types, Dispatcher


async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")

    await message.answer("\n".join(text))


def register_help_handler(dp: Dispatcher):
    dp.register_message_handler(bot_help, commands='help')
