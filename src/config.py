import os

from pydantic import AnyHttpUrl
from pydantic_settings import SettingsConfigDict, BaseSettings


class Config(BaseSettings):

    BOT_TOKEN: str
    API_URL: AnyHttpUrl = 'https://api.tvmaze.com/'
    print(os.path.abspath(".env"))
    model_config = SettingsConfigDict(env_file=os.path.abspath(".env"))


config = Config()
