from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = 'Your_token' #Ключ Telegram-бота
bot = Bot(token=api) # Обект бота
dp = Dispatcher(bot, storage=MemoryStorage()) # Диспатчер для обработки событий


@dp.message_handler(commands=['start'])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")
@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
