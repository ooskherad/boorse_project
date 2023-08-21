import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


class Stock(BaseModel):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name_fa: Mapped[str] = mapped_column(String(60), nullable=True)
    symbol: Mapped[str] = mapped_column(String(30),  nullable=True)
    created_at: Mapped[datetime.datetime] = DataType().created_at

