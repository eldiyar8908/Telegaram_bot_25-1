from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.config import bot
from aiogram import types, Dispatcher
from data_base.bot_db import sql_command_random


async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f'Бот запущен, {message.from_user.first_name}')


async def mem(message: types.Message):
    photo = open("media/mem.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)
    photo.close()


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('2nd question!', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Кто изобрел первый цифровой компьютер?'
    answers = [
        'Конрад Цузе',
        "Илон Маск",
        'Джефф Безос',
        'Стив Джобс',
        "Марк Цукерберг",
        'Альберт Энштейн'
    ]
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )







def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz1, commands=['quiz1'])
    dp.register_message_handler(sql_command_random, commands=['random_user'])
