import datetime
from typing import List

from sqlalchemy import text

from databse.models.stock_client_types import StockClientType, factory_stock_client_type
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from stock_info.client_types.models import ClientTypeAllModel


def save_client_types_data(data: List[ClientTypeAllModel]):
    save_in_postgres(data)


def save_in_postgres(data: List[ClientTypeAllModel]):
    session = DEFAULT_SESSION_FACTORY()

    query = text("""
            select * from (
          select *,
                 row_number() over (partition by id order by id desc) as rn
          from stock_client_types
        ) t
        where rn = 1
        order by id;
    """)
    client_type_in_db = [make_expression(factory_stock_client_type(**r._mapping)) for r in session.execute(query).all()]

    if isinstance(data, ClientTypeAllModel):
        data = [data]
    for item in data:
        client = StockClientType()
        client.stock_id = item.stock_id
        client.last_price = item.last_price
        client.transaction_at = item.transaction_at
        client.number_of_real_in_buy = item.number_of_real_in_buy
        client.number_of_legal_in_buy = item.number_of_legal_in_buy
        client.number_of_real_in_sell = item.number_of_real_in_sell
        client.number_of_legal_in_sell = item.number_of_legal_in_sell
        client.volume_of_real_in_sell = item.volume_of_real_in_sell
        client.volume_of_real_in_buy = item.volume_of_real_in_buy
        client.volume_of_legal_in_buy = item.volume_of_legal_in_buy
        client.volume_of_legal_in_sell = item.volume_of_legal_in_sell

        if make_expression(client) not in client_type_in_db:
            session.add(client)
    session.commit()


def make_expression(r):
    return str(r.stock_id) + str(r.transaction_at) + str(r.number_of_legal_in_sell) + str(
        r.number_of_real_in_sell) + str(
        r.number_of_real_in_buy) + str(r.number_of_legal_in_buy)
