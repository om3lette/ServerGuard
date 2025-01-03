import os
from enum import IntEnum

from dotenv import load_dotenv


class ExitStatus(IntEnum):
    ERROR = 1
    EARLY_RETURN = 2


load_dotenv()


SERVER_ADDRESS: str = os.getenv("SERVER_ADDRESS", "")
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

ADMINS: list[str] = [f"@{admin_username}" for admin_username in os.getenv("ADMINS", "").split()]
ADMIN_IDS: list[int] = list(map(int, os.getenv("ADMIN_IDS", "").split()))

MAX_RETRIES: int = 3
SECONDS_BETWEEN_RETRIES: int = 20
