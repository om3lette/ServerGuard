import logging

import aiomcrcon
from src.constants import SERVER_ADDRESS, RCON_PORT


class RconHandler:
    def __init__(self, rcon_password: str):
        self.__password: str = rcon_password
        self.__address: str = SERVER_ADDRESS.split(':')[0]

    @property
    def is_configured(self):
        return self.__password is not None and self.__password != ""

    async def execute(self, command: str) -> str | None:
        try:
            async with aiomcrcon.Client(self.__address, self.__password, RCON_PORT) as client:
                return await client.command(command.replace('/', '', 1))
        except (OSError, TimeoutError) as e:
            if e == OSError:
                logging.critical("Unable to connect to rcon. Check firewall settings and port availability")
            else:
                logging.critical("Unable to connect to rcon. Connection timed out. Check the provided SERVER_ADDRESS for errors")
            return None
