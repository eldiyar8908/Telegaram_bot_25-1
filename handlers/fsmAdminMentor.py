from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import mentors_id
from random import randint
from config import ADMINS


class FSMAdmin(StatesGroup):
    mentors_id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.chat.type == 'private':
            await FSMAdmin.mentors_id.set()
            while True:
                id = randint(100000,999999)
                if id not in mentors_id:
                    async with state.proxy() as data:
                        data['mentors_id'] = id
                    mentors_id.append(id)
                    break
            await FSMAdmin.next()
            await message.answer('Как зовут?')
        else:
            await message.answer("Пиши в личку!")
    else:
        await message.answer('Только админы!!')


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


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await state.finish()
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
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)