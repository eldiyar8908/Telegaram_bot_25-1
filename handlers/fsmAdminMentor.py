from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import mentors_id, ADMINS
from data_base.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS and message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer('id?')

    elif message.from_user.id not in ADMINS:
        await message.answer('Ты не админ!')
    elif message.chat.type != 'private':
        await message.answer('пиши в личку!')

async def load_id(message: types.Message, state: FSMContext):
    if message.text.isnumeric():
        async with state.proxy() as data:
            data['id'] = message.text
        await FSMAdmin.next()
        await message.answer("Имя?")

async def load_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое направление?")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько лет?')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) <= 0:
            await message.answer("Только положительные числа!")
        else:
            async with state.proxy() as data:
                data['age'] = message.text
            await FSMAdmin.next()
            await message.answer("Укажите группу.")
    except ValueError:
        await message.answer("Числа брат, числа")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(
            f"{data['name']}, {data['age']}, {data['direction']}, {data['group']}, "
        )
        await message.answer('всё правильно?')
        await FSMAdmin.next()


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer('ты зареган!!')

    elif message.text.lower() == "нет":
        await state.finish()
    else:
        await message.answer("Нипонял!?")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Cancled")


def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)



