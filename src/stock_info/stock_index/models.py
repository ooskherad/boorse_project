from typing import List

from stock_info.stock_indentifier.models import Stock


class Index:
    def __init__(self, insCode, lVal30, hEven, xDrNivJIdx004, xPhNivJIdx004, xPbNivJIdx004, xVarIdxJRfV, indexChange,
                 **kwargs):
        self.identifier = insCode
        self.name = lVal30
        self.time = hEven
        self.value = xDrNivJIdx004
        self.value_max = xPhNivJIdx004
        self.value_min = xPbNivJIdx004
        self.change_percent = xVarIdxJRfV
        self.change = indexChange

        self.stocks: List[Stock] = []

    def add_stock(self, stock):
        self.stocks.append(stock)
