import datetime
from typing import List

from databse.models.stock_client_types import StockClientType
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from stock_info.client_types.models import ClientTypeAllModel


def save_client_types_data(data: List[ClientTypeAllModel]):
    save_in_postgres(data)


def save_in_postgres(data: List[ClientTypeAllModel]):
    session = DEFAULT_SESSION_FACTORY()

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

        session.add(client)
    session.commit()
