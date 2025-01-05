import logging

import aiomcrcon
from src.constants import SERVER_ADDRESS


class RconHandler:
    def __init__(self, rcon_password: str):
        self.password = rcon_password

    @property
    def is_configured(self):
        return self.password is not None and self.password != ""

    async def execute(self, command: str) -> str | None:
        try:
            async with aiomcrcon.Client(SERVER_ADDRESS, self.password) as client:
                return await client.command(command.replace('/', '', 1))
        except (OSError, TimeoutError) as e:
            if e == OSError:
                logging.critical("Unable to connect to rcon. Check firewall settings and port availability")
            else:
                logging.critical("Unable to connect to rcon. Connection timed out. Check the provided SERVER_ADDRESS for errors")
            return None
