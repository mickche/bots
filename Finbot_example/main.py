
import asyncio
from bot import run_bot

from routers import root_router


async def main():
    await run_bot()


if __name__ == "__main__":
    asyncio.run(main())
