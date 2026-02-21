
from aiogram import Router

from .timer import timer_router
from .calculator import calc_router


root_router = Router()
root_router.include_routers(
    timer_router,
    calc_router
)
