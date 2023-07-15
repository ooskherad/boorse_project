import json
from typing import List

import requests

from stock_info.stock_indentifier.models import Stock
from stock_info.stock_index.models import Index
from stock_info.urls import MARKET_INDICES, DEFAULT_HEADERS, INDEX_STOCKS


class StockIndex:
    def __init__(self):
        self.data: List[Index] = []
        self.__data = []

    def req(self, url):
        resp = requests.get(url, headers=DEFAULT_HEADERS)
        if resp.status_code == 200:
            self.__data = json.loads(resp.text).get('indexB1')

    def model_data(self):
        for item in self.__data:
            self.data.append(Index(**item))

    def get_data(self):
        self.data.clear()
        markets = (1, 2)  # 1 for boorse and 2 for faraboorse
        for market in markets:
            self.req(MARKET_INDICES.format(market=market))
            self.model_data()

        for index in self.data:
            resp = requests.get(INDEX_STOCKS.format(index_id=index.identifier), headers=DEFAULT_HEADERS)
            if resp.status_code == 200:
                stocks = json.loads(resp.text)
                for stock in stocks["indexCompany"]:
                    stock = stock["instrument"]
                    index.add_stock(Stock(identifier=stock["insCode"], name_fa=stock["lVal30"]))
