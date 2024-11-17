import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import Config
from handlers import router
from keyboard import create_main_keyboard

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота, диспетчера и маршрутизатора
bot = Bot(token=Config.TELEGRAM_API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
