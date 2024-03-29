import datetime
from typing import List

from sqlalchemy import text

from database.models.stock_client_types import StockClientType, factory_stock_client_type
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from stock_info.client_types.models import ClientTypeAllModel


def save_client_types_data(data: List[ClientTypeAllModel]):
    save_in_postgres(data)


def save_in_postgres(data: List[ClientTypeAllModel]):
    session = DEFAULT_SESSION_FACTORY()

    query = text("""
            select * from (
          select *,
                 row_number() over (partition by stock_id order by transaction_at desc) as rn
          from stock_client_types
          where stock_id = ANY(:stock_ids)
        ) t
        where rn = 1
        order by id;
    """)

    stock_ids = [item.stock_id for item in data]
    last_client_type = session.execute(query, {'stock_ids': stock_ids}).fetchall()
    client_type_in_db = {}
    for r in last_client_type:
        r = r._mapping
        client_type_in_db[r["stock_id"]] = factory_stock_client_type(**r)

    if isinstance(data, ClientTypeAllModel):
        data = [data]
    for item in data:
        last_client = client_type_in_db.get(item.stock_id)
        if last_client and last_client.transaction_at.date() == item.transaction_at.date() and not (
                item.transaction_at.time() != last_client.transaction_at.time() and (
                last_client.number_of_real_in_sell < item.number_of_real_in_sell or
                last_client.number_of_real_in_buy < item.number_of_real_in_buy or
                last_client.number_of_legal_in_sell < item.number_of_legal_in_sell or
                last_client.number_of_legal_in_buy < item.number_of_legal_in_buy)):
            continue
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

        session.add(client)

    try:
        session.commit()
    except Exception as e:
        pass


def make_expression(r):
    return str(r.stock_id) + str(r.transaction_at) + str(r.number_of_legal_in_sell) + str(
        r.number_of_real_in_sell) + str(
        r.number_of_real_in_buy) + str(r.number_of_legal_in_buy)
