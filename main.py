from aiogram.utils import executor
import logging
from handlers import client, extra, call_back, fsmAdminMentor
from handlers.config import dp


fsmAdminMentor.register_handlers_anketa(dp)
call_back.register_handlers_callback(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)