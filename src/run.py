import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import config
from bot.handle.user import router

bot = Bot(token=config.BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(storage=storage)


async def on_startup(bot: Bot):
    print("Start Bot")


async def on_shutdown(bot: Bot):
    print("End bot")


async def mein():
    dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(mein())
    except KeyboardInterrupt:
        print("Exit")
