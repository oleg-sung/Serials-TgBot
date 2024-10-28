import os

from pydantic_settings import SettingsConfigDict, BaseSettings


class Config(BaseSettings):

    BOT_TOKEN: str
    API_URL: str = 'https://api.tvmaze.com/'
    REST_TIMEOUT: int = 20

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    model_config = SettingsConfigDict(env_file=os.path.abspath(".env"))


config = Config()
