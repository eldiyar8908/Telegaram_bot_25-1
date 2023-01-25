import asyncio

from aiogram.utils import executor
import logging
from handlers import client, extra, call_back, fsmAdminMentor, notification
from handlers.config import dp
from data_base.bot_db import sql_create

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

notification.register_message_notification(dp)
fsmAdminMentor.register_handlers_anketa(dp)
call_back.register_handlers_callback(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)