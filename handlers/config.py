from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()


TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = (1147816412, )
mentors_id = []