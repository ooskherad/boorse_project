import datetime

from sqlalchemy import BigInteger, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import BaseModel


def factor_stock_price_detail(stock_id, transaction_volume, transaction_count, transaction_at, price, **kwargs):
    model = StockPriceDetail()
    model.price = price
    model.stock_id = stock_id
    model.transaction_count = transaction_count
    model.transaction_volume = transaction_volume
    model.transaction_at = transaction_at


class StockPriceDetail(BaseModel):
    __tablename__ = "stock_price_details"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    stock_id: Mapped[int] = mapped_column(BigInteger)
    transaction_volume: Mapped[int] = mapped_column(BigInteger)
    transaction_count: Mapped[int] = mapped_column(Integer)
    transaction_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    price: Mapped[int] = mapped_column(Integer)
