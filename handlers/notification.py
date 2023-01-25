import aioschedule
import asyncio
from aiogram import types, Dispatcher
from handlers.config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer('ok')


async def last_day():
    for id in chat_id:
        await bot.send_message(id, 'Завтра выходной.')


async def scheduler():
    aioschedule.every().saturday.at('20:30').do(last_day)
    while 1:
        await aioschedule.run_pending()
        await asyncio.sleep(60)




def register_message_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)