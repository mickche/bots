
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()


@start_router.message(Command("start"))
async def handle_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Калькулятор", callback_data="start_router")
    builder.button(text="Таймер", callback_data="write_router")

    await message.reply(
        text="Привіт я КалкТаймер бот. ",
        reply_markup=builder.as_markup()
    )
