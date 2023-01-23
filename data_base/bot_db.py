import sqlite3


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



# async def sql_command_insert(state):
#     async with state.proxy() as data:
#         cursor.execute("INSERT INTO mentors "
#                        "(name, direction, age, gruppa) VALUES "
#                        "(?, ?, ?, ?)", tuple(data.values()))
#         db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?,?)", tuple(data.values()))
        db.commit()
