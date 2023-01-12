from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging


TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, f'Бот запущен, {message.from_user.first_name}')


@dp.message_handler(commands=['quiz1'])
async def quiz1(message: types.Message):
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
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )


@dp.message_handler(commands=['quiz2'])
async def quiz1(message: types.Message):
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
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4
    )


@dp.message_handler()
async def int_or_str(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text) * int(message.text))
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)