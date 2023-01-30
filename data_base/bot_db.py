import sqlite3
import random
from handlers.config import bot
from aiogram import types


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()

    if db:
        print('Connected')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY , "
               "name VARCHAR (100),"
               "direction VARCHAR (100),"
               "age INTEGER,"
               "gruppa TEXT)")
    db.commit()



async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message: types.Message):
    result = cursor.execute('SELECT * FROM mentors').fetchall()
    random_user = random.choice(result)
    await bot.send_message(
        message.from_user.id,
        random_user[-1],
        text=f'{random_user[1]}, {random_user[2]}, {random_user[3]}, {random_user[4]},'
    )


async def sql_command_all():
    return cursor.execute('SELECT * FROM mentors').fetchall()


async def sql_command_delete(user_id):
    cursor.execute('DELETE FROM mentors WHERE id = ?', (user_id,))
    db.commit()