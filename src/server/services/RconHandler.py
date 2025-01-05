import aiomcrcon
from src.constants import SERVER_ADDRESS


class RconHandler:
    def __init__(self, rcon_password: str):
        self.password = rcon_password

    async def execute(self, command: str) -> str | None:
        try:
            async with aiomcrcon.Client(SERVER_ADDRESS, self.password) as client:
                return await client.command(command.replace('/', '', 1))
        except OSError:
            return None
