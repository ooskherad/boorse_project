from sqlalchemy import create_engine, URL, NullPool
from sqlalchemy.orm import sessionmaker

from infrastructure.configs import config

DEFAULT_URl = URL.create("postgresql+psycopg2", username=config.POSTGRES_USER, password=config.POSTGRES_PASSWORD,
                         host=config.POSTGRES_HOST, port=config.POSTGRES_PORT, database=config.POSTGRES_DATABASE)

DEFAULT_ENGIN = create_engine(
    DEFAULT_URl,
    pool_size=10,
    max_overflow=2,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=config.DEBUG,
)

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=DEFAULT_ENGIN
)
