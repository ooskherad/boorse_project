import datetime

from sqlalchemy import String, BigInteger, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.postgres.data_types import DataType, BaseModel


class Stock(BaseModel):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name_fa: Mapped[str] = mapped_column(String(60), nullable=True)
    symbol_name: Mapped[str] = mapped_column(String(30), nullable=True)
    symbol_name_30: Mapped[str] = mapped_column(String(30), nullable=True)
    name_en: Mapped[str] = mapped_column(String(60), nullable=True)
    company_digit_code12: Mapped[str] = mapped_column(String(12), nullable=True)
    symbol_digit_code12: Mapped[str] = mapped_column(String(12), nullable=True)
    symbol_digit5: Mapped[str] = mapped_column(String(5), nullable=True)
    company_digit4: Mapped[str] = mapped_column(String(4), nullable=True)
    market: Mapped[str] = mapped_column(String(60), nullable=True)
    table_code: Mapped[int] = mapped_column(Integer, nullable=True)
    industry_group_code: Mapped[int] = mapped_column(Integer, nullable=True)
    industry_subgroup_code: Mapped[int] = mapped_column(Integer, nullable=True)
    industry_group_name: Mapped[str] = mapped_column(String(60), nullable=True)
    industry_subgroup_name: Mapped[str] = mapped_column(String(60), nullable=True)
    base_volume: Mapped[int] = mapped_column(BigInteger, nullable=True)
    total_stock_number: Mapped[int] = mapped_column(BigInteger, nullable=True)
    eps: Mapped[int] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime.datetime] = DataType().created_at
    creation_data: Mapped[dict] = mapped_column(JSONB, nullable=True)
