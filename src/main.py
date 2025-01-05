import sys
import asyncio
import logging

from src.server.router import server_router
from src.bot import bot
from src.handlers import rcon_handler

from aiogram import Dispatcher


async def main() -> None:
    dp: Dispatcher = Dispatcher()
    dp.include_router(server_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
