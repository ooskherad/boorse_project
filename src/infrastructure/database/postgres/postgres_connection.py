from sqlalchemy import create_engine, URL, NullPool
from sqlalchemy.orm import sessionmaker

from infrastructure.configs import config

DEFAULT_URl = URL.create("postgresql+psycopg2", username=config.POSTGRES_USER, password=config.POSTGRES_PASSWORD,
                         host=config.POSTGRES_HOST, port=config.POSTGRES_PORT, database=config.POSTGRES_DATABASE)

DEFAULT_ENGIN = create_engine(
    DEFAULT_URl,
    poolclass=NullPool,
    isolation_level="REPEATABLE READ",
    echo=config.DEBUG,
)

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=DEFAULT_ENGIN
)
