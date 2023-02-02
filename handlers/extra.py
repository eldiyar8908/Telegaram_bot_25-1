import os

from aiogram import types, Dispatcher
from handlers.config import bot, ADMINS
from random import randint
from pytube import YouTube

async def echo(message: types.Message):
    if message.text.startswith('https://www.youtube.com'):
        url = message.text
        video = YouTube(url=url)
        await bot.send_message(message.from_user.id, 'Скачивание началось. Ожидайте!')
        stream = video.streams.filter(progressive=True, file_extension='mp4')
        stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{video.title}' )
        with open(f'{message.chat.id}/{message.chat.id}_{video.title}', 'rb') as video1:
            await bot.send_video(message.chat.id, video=video1)
            os.remove(f'{message.chat.id}/{message.chat.id}_{video.title}')
    elif message.text.startswith('game'):
        if message.chat.type != 'private':
            if message.from_user.id not in ADMINS:
                await message.answer('Ты не админ! Иди, отдыхай)')
            else:
                a = randint(1,6)
                userID = message.chat.id
                if a == 1:
                    await bot.send_dice(userID, emoji='⚽')
                elif a == 2:
                    await bot.send_dice(userID, emoji='🏀')
                elif a == 3:
                    await bot.send_dice(userID, emoji='🎲')
                elif a == 4:
                    await bot.send_dice(userID, emoji='🎯')
                elif a == 5:
                    await bot.send_dice(userID, emoji='🎳')
                elif a == 6:
                    await bot.send_dice(userID, emoji='🎰')
        else:
            await message.answer('Пиши в группу!')
    elif message.text == '!pin':
        try:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        except AttributeError:
            bot.send_message(message.from_user.id, 'Сообщение должно быть ответом на длугое сообщение!!!')
    elif message.chat.type == 'private':
        if message.text.isdigit():
            await bot.send_message(chat_id=message.chat.id, text=int(message.text) * int(message.text))
        else:
            await bot.send_message(chat_id=message.chat.id, text=message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
