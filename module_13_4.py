from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
import data



api = f'{data.token_LB}'  # Ключ Telegram-бота
bot = Bot(token=api)  # Обект бота
# Диспатчер для обработки событий
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight=int(message.text))
    await message.answer('Укажите свой пол (м\ж):') # Задаём пол чтоб данные были точнее
    await UserState.sex.set()

@dp.message_handler(state=UserState.sex) 
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    await UserState.sex.set()
    data =  await state.get_data()
    calories_form = 10.0 * data['weight'] + 6.25 * data['growth'] - 5.0 * data['age']
    calories = calories_form + 5 if data['sex'] == 'м' else calories_form - 161

    await message.answer(f'Ваша норма в калориях: {calories}')
    await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

