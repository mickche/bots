
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from data import save_data


write_router = Router()


CATEGORIES = [
    "Їжа", "Спорт"
]


@write_router.message()
async def handle_write(message: Message):
    parts = message.text.split()

    if len(parts) < 2:
        return await message.reply(
            text="Та написав щось не так. Повинно бути і НАЗВА і ЦІНА"
        )

    name = ' '.join(parts[:-1])
    price = parts[-1]

    try:
        price = float(price.replace(",", "."))

    except Exception:
        return await message.reply(
            text="Та написав щось не так. Напиши нормальне число"
        )

    try:
        keyboard = InlineKeyboardBuilder()
        for category in CATEGORIES:
            keyboard.add(InlineKeyboardButton(
                text=category,
                callback_data=f"save~{name}~{price}~{category}"
            ))
        keyboard.adjust(3)

        return await message.reply(
            text=f"<b>{name}</b> - <i>{price}</i>"
                 f"\n\nОбери категорію щоб зберегти",
            parse_mode="html",
            reply_markup=keyboard.as_markup()
        )

    except Exception:
        return await message.reply(
            text="Та написав щось не так. Можливо витрата завелика"
        )


@write_router.callback_query(F.data.startswith("save"))
async def handle_write(callback: CallbackQuery):
    action, name, price, category = callback.data.split("~")
    price = float(price)

    save_data(callback.from_user.id, {"name": name, "price": price, "category": category})

    keyboard = InlineKeyboardBuilder()
    await callback.message.edit_text(
        text=f"<b>{name}</b> - <i>{price}</i>"
             f"\nКатегорія: <i>{category}</i>"
             f"\n\n<i>Дані сбережено</i>",
        parse_mode="html",
        reply_markup=keyboard.as_markup()
    )
