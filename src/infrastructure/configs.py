from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG = True
    PORT = 8008

    # POSTGRES CONFIGS
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "SnkECs2DM1IA13MbobWE1yLb0GMd6FIs"
    POSTGRES_DATABASE = "boorse"
    POSTGRES_PORT = "30654"
    POSTGRES_HOST = "38928227-af07-41b4-82f7-c21f09f41e43.hsvc.ir"

    INFLUX_URL = ""
    INFLUX_TOKEN = ""
    INFLUX_ORG = ""

    class Config:
        case_sensitive = False
        env_file = '../.env'
        env_file_encoding = 'utf-8'


config = Config()
