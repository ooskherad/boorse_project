from typing import List
from influxdb_client import Point
from sqlalchemy import text

from database.models.stock_price import StockPrice
from database.models.stock_price_detail import StockPriceDetail, factor_stock_price_detail
from infrastructure.database.influx.connection import InfluxDb
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from stock_info.market_watch.models import MarketWatchModel


def save_market_watch_data(data: List[MarketWatchModel]):
    save_in_postgres(data)


def make_expression(param):
    pass


def save_in_postgres(data: List[MarketWatchModel]):
    session = DEFAULT_SESSION_FACTORY()
    query = text("""
                select * from (
              select *,
                     row_number() over (partition by stock_id order by id desc) as rn
              from stock_price_details
              where stock_id = ANY(:stock_ids)
            ) t
            where rn = 1
            order by id;
        """)
    stock_ids = [int(item.stock_id) for item in data]
    last_prices = session.execute(query, {'stock_ids': stock_ids}).fetchall()
    last_prices_in_db = [make_expression(factor_stock_price_detail(**r._mapping)) for r in last_prices]
    if isinstance(data, MarketWatchModel):
        data = [data]
    try:
        for item in data:
            price_detail = StockPriceDetail()
            price_detail.price = item.price_last
            price_detail.transaction_at = item.transaction_at
            price_detail.stock_id = item.stock_id
            price_detail.transaction_count = item.transaction_count
            price_detail.transaction_volume = item.transaction_volume
            if make_expression(price_detail) in last_prices_in_db:
                continue
            session.add(price_detail)

            # price = StockPrice()
            # price.stock_id = item.stock_id
            # price.price_last = item.price_last
            # price.price_authorized_min = item.price_authorized_min
            # price.price_max = item.price_max
            # price.price_min = item.price_min
            # price.price_authorized_max = item.price_authorized_max
            # price.transaction_at = item.transaction_at
            # price.price_close = item.price_close
            # price.price_first = item.price_first
            # price.price_yesterday = item.price_yesterday
            # price.transaction_count = item.transaction_count
            # price.transaction_volume = item.transaction_volume
            # session.add(price)

    except Exception as e:
        print()
    session.commit()


def _save_in_influx(data: List[MarketWatchModel]):
    insert_data = []
    for row_data in data:
        point: Point
        point = Point("stock_prices").tag('id', row_data.stock_id)
        point = point.field("field", row_data.volume)
        point = point.field("price", row_data.price)
        point = point.field("transaction_at", row_data.transaction_at)
        insert_data.append(point)

    write_api = InfluxDb.write_api()
    write_api(records=insert_data, bucket=InfluxDb.DEFAULT_BUCKET)
