from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG = True
    PORT = 8008

    # POSTGRES CONFIGS
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "1234"
    POSTGRES_DATABASE = "postgres"
    POSTGRES_PORT = "5433"
    POSTGRES_HOST = "194.33.127.252"

    INFLUX_URL = ""
    INFLUX_TOKEN = ""
    INFLUX_ORG = ""

    class Config:
        case_sensitive = False
        env_file = './.env'
        env_file_encoding = 'utf-8'


config = Config()
