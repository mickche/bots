
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()


@start_router.message(Command("start"))
async def handle_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Калькулятор", url="https://aiogram.dev/")
    builder.button(text="Таймер", url="https://github.com/")

    await message.reply(
        text="Привіт я КалкТаймер бот. ",
        reply_markup=builder.as_markup()
    )
