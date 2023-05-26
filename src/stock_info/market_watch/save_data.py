from typing import List
from influxdb_client import Point

from infrastructure.database.influx.connection import InfluxDb
from stock_info.market_watch.models import MarketWatchModel


def save_market_watch_data(data: List[MarketWatchModel]):
    _save_in_influx(data)


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
