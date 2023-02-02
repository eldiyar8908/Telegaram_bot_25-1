from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.config import bot
from aiogram import types, Dispatcher


async def check1(call: types.CallbackQuery):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001195426632', user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, 'Спасибо за подписку!')
            break

async def check(call: types.CallbackQuery):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001195426632', user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, 'Спасибо за подписку!')
            break


async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('3rd question', callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Кто изобрел первый поезд?'
    answers = [
        "Марк Цукерберг",
        'Джефф Безос',
        "Илон Маск",
        'Стив Джобс',
        'Ричард Тревитик',
        'Альберт Энштейн'
    ]
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        reply_markup=markup
    )


async def quiz3(call: types.CallbackQuery):
    question = 'Кто придумал интернет?'
    answers = [
        "Марк Цукерберг",
        'Джефф Безос',
        "Илон Маск",
        'Стив Джобс',
        'Ричард Тревитик',
        'Винт Серф'
    ]
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, text='button_call_1')
    dp.register_callback_query_handler(quiz3, text='button_call_2')
    dp.register_callback_query_handler(check, text='check')
