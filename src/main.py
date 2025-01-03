import sys
import asyncio
import logging

from src.constants import BOT_TOKEN, SERVER_ADDRESS
from src.utils import check_for_exit_condition
from src.server.router import server_router
from src.bot import bot

from aiogram import Dispatcher


async def main() -> None:
    check_for_exit_condition(BOT_TOKEN, lambda x: x == "" or len(x) != 46, "Incorrect bot token provided")
    check_for_exit_condition(SERVER_ADDRESS, lambda x: x == "", "Incorrect server address provided")

    dp: Dispatcher = Dispatcher()
    dp.include_router(server_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
