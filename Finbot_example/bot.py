
from aiogram import Bot, Dispatcher
from routers import root_router


bot = Bot(token="")
dp = Dispatcher()

dp.include_router(root_router)


async def run_bot():
    await dp.start_polling(bot)
