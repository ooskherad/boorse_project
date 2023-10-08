import datetime

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


def factory_stock_client_type(id, stock_id, number_of_real_in_buy, number_of_legal_in_buy, number_of_legal_in_sell,
                              number_of_real_in_sell, volume_of_real_in_buy, volume_of_real_in_sell,
                              volume_of_legal_in_sell, volume_of_legal_in_buy, last_price, transaction_at,
                              created_at, **kwargs):
    stock_client_type = StockClientType()
    stock_client_type.id = id
    stock_client_type.stock_id = stock_id
    stock_client_type.number_of_real_in_buy = number_of_real_in_buy
    stock_client_type.number_of_legal_in_buy = number_of_legal_in_buy
    stock_client_type.number_of_legal_in_sell = number_of_legal_in_sell
    stock_client_type.number_of_real_in_sell = number_of_real_in_sell
    stock_client_type.volume_of_real_in_buy = volume_of_real_in_buy
    stock_client_type.volume_of_real_in_sell = volume_of_real_in_sell
    stock_client_type.volume_of_legal_in_sell = volume_of_legal_in_sell
    stock_client_type.volume_of_legal_in_buy = volume_of_legal_in_buy
    stock_client_type.last_price = last_price
    stock_client_type.transaction_at = transaction_at
    stock_client_type.created_at = created_at
    return stock_client_type


class StockClientType(BaseModel):
    __tablename__ = "stock_client_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    stock_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("stocks.id"))
    number_of_real_in_buy: Mapped[int] = mapped_column()
    number_of_legal_in_buy: Mapped[int] = mapped_column()
    number_of_legal_in_sell: Mapped[int] = mapped_column()
    number_of_real_in_sell: Mapped[int] = mapped_column()
    volume_of_real_in_buy: Mapped[int] = mapped_column()
    volume_of_real_in_sell: Mapped[int] = mapped_column()
    volume_of_legal_in_sell: Mapped[int] = mapped_column()
    volume_of_legal_in_buy: Mapped[int] = mapped_column()
    last_price: Mapped[int] = mapped_column()
    transaction_at: Mapped[datetime.datetime] = DataType().created_at
    created_at: Mapped[datetime.datetime] = DataType().created_at
