import asyncio
from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from start import start
from aiogram import Router

timer_router = Router()

@timer_router.callback_query(F.data == "set_timer")
async def timer_info(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Введіть час (сек або хв:сек).\nНаприклад: 10 або 1:30", 
        reply_markup=InlineKeyboardBuilder().row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")).as_markup()
    )

@timer_router.message()
async def handle_everything(message: types.Message):
    text = message.text.strip()
    

    if ":" in text or text.isdigit():
        try:
            if ":" in text:
                p = text.split(":")
                total_sec = int(p[0]) * 60 + int(p[1])
            else:
                total_sec = int(text)
            
            msg = await message.answer(f"⏳ Таймер запущено: {total_sec} сек")
            for i in range(total_sec, -1, -1):
                if i == 0:
                    await msg.edit_text("⏰ Час вийшов!", reply_markup=start())
                elif i % 5 == 0 or i < 5:
                    await msg.edit_text(f"⏳ Залишилось: {i // 60:02d}:{i % 60:02d}")
                await asyncio.sleep(1)
            return
        except:
            pass