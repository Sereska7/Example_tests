from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST"]

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    DB_URL: str
    TEST_DB_URL: str

    model_config = SettingsConfigDict(env_file="/.env-non-dev")


settings = Settings()
