import datetime


class ClientTypeAllModel:
    stock_id: str
    number_of_real_in_buy: int
    number_of_legal_in_buy: int
    number_of_legal_in_sell: int
    number_of_real_in_sell: int
    volume_of_real_in_buy: int
    volume_of_real_in_sell: int
    volume_of_legal_in_sell: int
    volume_of_legal_in_buy: int
    last_price: int
    transaction_at: datetime.datetime

    def __init__(self, stock_id: str, number_of_real_in_buy: int,
                 number_of_legal_in_buy: int,
                 number_of_legal_in_sell: int,
                 number_of_real_in_sell: int,
                 volume_of_real_in_buy: int,
                 volume_of_real_in_sell: int,
                 volume_of_legal_in_sell: int,
                 volume_of_legal_in_buy: int):
        self.stock_id: str = stock_id
        self.number_of_real_in_buy: int = number_of_real_in_buy
        self.number_of_legal_in_buy: int = number_of_legal_in_buy
        self.number_of_legal_in_sell: int = number_of_legal_in_sell
        self.number_of_real_in_sell: int = number_of_real_in_sell
        self.volume_of_real_in_buy: int = volume_of_real_in_buy
        self.volume_of_real_in_sell: int = volume_of_real_in_sell
        self.volume_of_legal_in_sell: int = volume_of_legal_in_sell
        self.volume_of_legal_in_buy: int = volume_of_legal_in_buy
