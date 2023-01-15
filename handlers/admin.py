from aiogram import types
from random import randint
from config import bot, ADMINS


async def games(message: types.Message):
    if message.text.startswith('game'):
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

def register_handlers_admin(dp):
    dp.register_message_handler(games)
