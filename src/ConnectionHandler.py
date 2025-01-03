import asyncio
import logging

from mcstatus import JavaServer
from typing import Callable

from mcstatus.status_response import JavaStatusPlayers

from .constants import MAX_RETRIES, SECONDS_BETWEEN_RETRIES
from aiogram.types import Message

from .utils import default_ping_error_callback


class ConnectionHandler:

    def __init__(self, server_address: str):
        self.server_address: str = server_address
        self.connection: JavaServer = JavaServer.lookup(self.server_address)

    async def is_connected(self, error_callback: Callable = lambda *args: None) -> bool:
        attempt_number: int = 1
        while attempt_number <= MAX_RETRIES:
            try:
                await self.connection.async_ping()
                return True
            except ConnectionRefusedError:
                logging.error(f"Ping №{attempt_number} failed")
                # Attempt number, is attempt final
                await error_callback(attempt_number, attempt_number == MAX_RETRIES)
                if attempt_number != MAX_RETRIES:
                    await asyncio.sleep(SECONDS_BETWEEN_RETRIES)
                attempt_number += 1
        logging.critical("Server is down. Calling admins")
        return False

    async def get_status_players(self) -> JavaStatusPlayers:
        return (await self.connection.async_status()).players

    async def query_players(self):
        try:
            return (await self.connection.async_query()).players
        except TimeoutError:
            logging.critical("'query' has to be enabled in a server's server.properties file!")
            return None

    async def execute(self, request_message: Message, func: Callable) -> tuple[bool, any]:
        if not await self.is_connected(lambda x, y: default_ping_error_callback(request_message, x, y)):
            return False, None

        return True, await func()
