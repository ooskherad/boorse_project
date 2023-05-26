import datetime


class MarketWatchModel:
    def __init__(self, stock_id, price, volume, transaction_at = None):
        self.stock_id: str = stock_id
        self.price: int = price
        self.volume: int = volume
        self.transaction_at: datetime.datetime = transaction_at
