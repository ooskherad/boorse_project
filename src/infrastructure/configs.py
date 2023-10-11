from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG = True
    PORT = 8008

    # POSTGRES CONFIGS
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    POSTGRES_DATABASE = ""
    POSTGRES_PORT = ""
    POSTGRES_HOST = ""

    INFLUX_URL = ""
    INFLUX_TOKEN = ""
    INFLUX_ORG = ""

    class Config:
        case_sensitive = False
        env_file = './.env'
        env_file_encoding = 'utf-8'


config = Config()
