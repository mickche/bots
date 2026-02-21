
from aiogram import Bot, Dispatcher
from routers import root_router
from pathlib import Path
from dotenv import dotenv_values


env_path = Path(__file__).parent.parent / ".env.local"

config = dotenv_values(env_path)

bot = Bot(token=config["TOKEN"])
dp = Dispatcher()

dp.include_router(root_router)


async def run_bot():
    await dp.start_polling(bot)
