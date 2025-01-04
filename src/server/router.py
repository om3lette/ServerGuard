from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

from src.handlers import connection_handler
from src.response_messages import PING_SUCCESS_MESSAGE, PLAYERS_NUMBER_MESSAGE, PLAYERS_ONLINE_MESSAGE, \
    QUERY_NOT_ENABLED_ERROR_MESSAGE, NO_PLAYERS_ONLINE_MESSAGE

server_router: Router = Router()


@server_router.message(Command("is_alive"))
async def check_server_status(message: Message):
    [is_alive, response_time] = await connection_handler.execute(message, connection_handler.connection.async_ping)
    if not is_alive:
        return
    await message.reply(PING_SUCCESS_MESSAGE.format(latency=round(response_time, 2)))


@server_router.message(Command("current_online"))
async def players_number(message: Message):
    [is_alive, players] = await connection_handler.execute(message, connection_handler.get_status_players)
    if not is_alive:
        return
    await message.reply(PLAYERS_NUMBER_MESSAGE.format(current_number=players.online, capacity=players.max))


@server_router.message(Command("players_online"))
async def players_list(message: Message):
    [is_alive, players_query] = await connection_handler.execute(message, connection_handler.query_server)
    if not is_alive:
        return
    if players_query is None:
        await message.reply(QUERY_NOT_ENABLED_ERROR_MESSAGE, parse_mode=ParseMode.MARKDOWN_V2)
        return
    players_ol: list[str] = [f"{i}. {username}" for i, username in enumerate(players_query.players.names, 1)]
    players_text: str = "\n".join(players_ol) if len(players_ol) != 0 else NO_PLAYERS_ONLINE_MESSAGE
    await message.reply(PLAYERS_ONLINE_MESSAGE.format(players=players_text))
