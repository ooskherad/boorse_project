import datetime

import requests
from sqlalchemy import text

from database.models import Stock
from database.models.stock_price import StockPrice
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from infrastructure.helper.utils import convert_string_to_time
from infrastructure.http_request import DEFAULT_HEADERS, get

url = "http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceDailyList/{stock_id}/0"


def get_stock_price_worker():
    session = DEFAULT_SESSION_FACTORY()
    query = text("""
                    select * from (
                  select *,
                         row_number() over (partition by stock_id order by transaction_at desc) as rn
                  from stock_prices
                ) t
                where rn = 1
                order by id;
            """)
    stock_last_prices = {}
    for item in session.execute(query).all():
        item = item._mapping
        stock_last_prices[item["stock_id"]] = item["transaction_at"]
    stocks = session.query(Stock).filter(~Stock.industry_group_code.in_([68, 69, 56])).all()
    for stock in stocks:
        resp = get(url.format(stock_id=stock.id))
        data = resp.json()
        for price in data["closingPriceDaily"]:
            h_even = convert_string_to_time(str(price["hEven"])).time()
            d_even = datetime.datetime.strptime(str(price["dEven"]), "%Y%m%d").date()
            transaction_at = datetime.datetime.combine(d_even, h_even)
            if stock_last_prices.get(stock.id) and stock_last_prices.get(stock.id) >= transaction_at:
                continue
            price_model = StockPrice()
            price_model.stock_id = stock.id
            price_model.transaction_at = transaction_at
            price_model.transaction_count = price["zTotTran"]
            price_model.transaction_volume = price["qTotTran5J"]
            price_model.price_yesterday = price["priceYesterday"]
            price_model.price_min = price["priceMin"]
            price_model.price_max = price["priceMax"]
            price_model.price_first = price["priceFirst"]
            price_model.price_close = price["pClosing"]
            price_model.price_last = price["pDrCotVal"]

            session.add(price_model)

        session.commit()

# get_stock_price_worker()
