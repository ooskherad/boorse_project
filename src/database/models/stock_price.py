import datetime

from sqlalchemy import BigInteger, Integer, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


class StockPrice(BaseModel):
    __tablename__ = "stock_prices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    stock_id: Mapped[int] = mapped_column(BigInteger)
    transaction_volume: Mapped[int] = mapped_column(BigInteger)
    transaction_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    price_first: Mapped[int] = mapped_column(Integer)
    price_last: Mapped[int] = mapped_column(Integer)
    price_close: Mapped[int] = mapped_column(Integer)
    transaction_count: Mapped[int] = mapped_column(Integer)
    price_min: Mapped[int] = mapped_column(Integer, nullable=True)
    price_max: Mapped[int] = mapped_column(Integer, nullable=True)
    price_yesterday: Mapped[int] = mapped_column(Integer, nullable=True)
    price_authorized_max: Mapped[int] = mapped_column(Integer, nullable=True)
    price_authorized_min: Mapped[int] = mapped_column(Integer, nullable=True)
