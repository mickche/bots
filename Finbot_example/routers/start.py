
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def handle_tart(message: Message):
    await message.reply(
        text="Привіт я фінансовий бот. "
             "Просто напиши мені свою витрату, а я запам'ятаю"
             "\n\nПриклад: <code>Атб 100</code>",
        parse_mode="html"
    )
