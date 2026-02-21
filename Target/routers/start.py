
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def handle_start(message: Message):
    await message.reply(
        text="Привіт я бот-калькулятор. Введи перше число ",
        parse_mode="html"
    )
