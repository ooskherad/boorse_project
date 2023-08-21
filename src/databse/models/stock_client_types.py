import datetime

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


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

