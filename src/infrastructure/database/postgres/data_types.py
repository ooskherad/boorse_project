from datetime import datetime

from sqlalchemy import DateTime, Column

from sqlalchemy.orm import declared_attr, declarative_base, registry


class CustomBase:

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

    pass


class DataType:
    @property
    def updated_at(self):
        return Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    @property
    def created_at(self):
        return Column(DateTime(timezone=True), default=datetime.now)


BaseModel = declarative_base()
MAPPER_REGISTRY = registry()