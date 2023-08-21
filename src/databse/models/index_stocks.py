import datetime

from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


class IndexStock(BaseModel):
    __tablename__ = "index_stocks"

    id: Mapped[int] = mapped_column(primary_key=True)
    stock_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("stocks.id"))
    index_id: Mapped[int] = mapped_column(BigInteger , ForeignKey("indices.id"))
    created_at: Mapped[datetime.datetime] = DataType().created_at

