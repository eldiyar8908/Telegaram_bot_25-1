from aiogram import types
from random import randint
from config import bot, ADMINS
from random import choice
from data_base.bot_db import sql_command_delete, sql_command_all


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


async def delete_user_db(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('ТЫ НЕ АДМИН!!!')
    else:
        users = await sql_command_all()
        random_user = choice(users)
        await bot.send_message(
            message.from_user.id,
            random_user[-1],
            text=f'{random_user[1]}, {random_user[2]}, {random_user[3]}, {random_user[4]},'
        )


def register_handlers_admin(dp):
    dp.register_message_handler(games)
    dp.register_message_handler(delete_user_db, lambda message: message.text
                                and message.text.startswith('delete '))



