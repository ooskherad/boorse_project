import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


class Index(BaseModel):
    __tablename__ = "indices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

