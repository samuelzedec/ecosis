from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()

ENV : Final[str] = os.getenv("ENV")
DATABASE_HOST : Final[str] = os.getenv("DATABASE_HOST")
DATABASE_PORT : Final[str] = os.getenv("DATABASE_PORT")