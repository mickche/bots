
from aiogram import Router

from .start import start_router
from .write import write_router


root_router = Router()
root_router.include_routers(
    start_router,
    write_router
)
