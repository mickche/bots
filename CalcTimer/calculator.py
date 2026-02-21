
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router


calc_router = Router()

def op_kb(n1):
    builder = InlineKeyboardBuilder()

    for op, symbol in [("add", "➕"), ("sub", "➖"), ("mul", "✖️"), ("div", "➗")]:
        builder.button(text=symbol, callback_data=f"op_{op}_{n1}")
    builder.adjust(2)
    return builder.as_markup()


@calc_router.callback_query(F.data == "calc_start")
async def ask_first_num(callback: types.CallbackQuery):
    await callback.message.edit_text("Введіть перше число просто у чат:")


@calc_router.message(F.text.regexp(r"^\d+[.,]?\d*$"))
async def process_first_number(message: types.Message):
    try:
        n1 = float(message.text.replace(',', '.'))
        await message.answer(f"Число: {n1}\nОберіть дію:", reply_markup=op_kb(n1))
    except ValueError:
        await message.answer("❌ Будь ласка, введіть коректне число.")

@calc_router.callback_query(F.data.startswith("op_"))
async def catch_op(callback: types.CallbackQuery):

    _, operation, n1 = callback.data.split("_")
    op_names = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
    
    await callback.message.edit_text(
        f"Ви обрали: {n1} {op_names[operation]}\nТепер введіть друге число (відповіддю на це повідомлення):"
    )



@calc_router.message()
async def handle_everything(message: types.Message):
    text = message.text.strip()