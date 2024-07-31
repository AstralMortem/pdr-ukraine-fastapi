import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent
PROJECT_DIR = BASE_DIR.parent
DOTENV = PROJECT_DIR / ".env"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, extra="ignore")
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, extra="ignore")

    # DATABASE SETTINGS
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_ECHO: bool = True

    @property
    def database_url(self) -> str:
        return f"{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def sync_db_path(self) -> str:
        return f"postgresql+psycopg2://{self.database_url}"

    @property
    def async_db_path(self) -> str:
        return f"postgresql+asyncpg://{self.database_url}"

    # PROJECT SETTINGS
    DEBUG: bool = True  # change on production
    PROJECT_NAME: str = "Fitness App"

    # SECURE SETTINGS
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    )

    # OAUTH
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_SECRET_KEY: str = os.getenv("GOOGLE_SECRET_KEY", "")


settings = Settings()
