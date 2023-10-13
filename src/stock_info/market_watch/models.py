import datetime


class MarketWatchModel:
    stock_id: int
    symbol: str
    name: str
    transaction_volume: int
    transaction_at: datetime.datetime
    price_first: int
    price_last: int
    price_close: int
    transaction_count: int
    price_min: int
    price_max: int
    price_yesterday: int
    eps: int
    price_authorized_max: int
    price_authorized_min: int
    total_stock_number: int

    def __init__(self, stock_id=None, price_first=None, price_last=None, price_close=None, transaction_count=None,
                 transaction_volume=None,
                 transaction_at=None, price_min=None, price_max=None, price_yesterday=None, eps=None,
                 price_authorized_max=None,
                 price_authorized_min=None, total_stock_number=None, symbol=None, name=None, **kwargs):
        self.stock_id: str = stock_id
        self.symbol: str = symbol
        self.name: str = name
        self.transaction_volume: int = transaction_volume
        self.transaction_at: datetime.datetime = transaction_at
        self.price_first: int = price_first
        self.price_last: int = price_last
        self.price_close: int = price_close
        self.transaction_count: int = transaction_count
        self.price_min: int = price_min
        self.price_max: int = price_max
        self.price_yesterday: int = price_yesterday
        self.eps: int = eps
        self.price_authorized_max: int = price_authorized_max
        self.price_authorized_min: int = price_authorized_min
        self.total_stock_number: int = total_stock_number
