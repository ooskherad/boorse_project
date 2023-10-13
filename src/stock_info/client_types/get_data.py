from typing import List

import requests

from stock_info.client_types.models import ClientTypeAllModel
from stock_info.client_types.save_data import save_client_types_data
from stock_info.market_watch.models import MarketWatchModel
from stock_info.urls import CLIENT_TYPE_ALL_URL
from infrastructure.http_request import DEFAULT_HEADERS, get


class ClientType:
    def __init__(self):
        self.data: List[ClientTypeAllModel] = []
        self.__raw_data: str = ""
        self.__data = []

    def req(self, url):
        resp = get(url)
        self.__raw_data = resp.text

    def split_data(self):
        data_ = self.__raw_data.split(';')
        for item in data_:
            items = item.split(",")
            if len(items) == 9:
                self.__data.append(items)

    def model_data(self):
        for split_data in self.__data:
            self.data.append(ClientTypeAllModel(
                stock_id=split_data[0],
                number_of_real_in_buy=split_data[1],
                number_of_legal_in_buy=split_data[2],
                number_of_legal_in_sell=split_data[6],
                number_of_real_in_sell=split_data[5],
                volume_of_real_in_buy=split_data[3],
                volume_of_real_in_sell=split_data[7],
                volume_of_legal_in_sell=split_data[8],
                volume_of_legal_in_buy=split_data[4],
            ))

    def get_data(self):
        self.data.clear()
        self.__data.clear()
        self.req(CLIENT_TYPE_ALL_URL)
        self.split_data()
        self.model_data()

    def save_data(self, last_changed_identifier: List[MarketWatchModel]):
        data = []
        self.data = sorted(self.data, key=lambda item: item.stock_id)
        last_changed_identifier = sorted(last_changed_identifier, key=lambda item: item.stock_id)
        for client_data in self.data:
            for stock_info in last_changed_identifier:
                if client_data.stock_id == stock_info.stock_id:
                    client_data.last_price = stock_info.price_last
                    client_data.transaction_at = stock_info.transaction_at
                    data.append(client_data)
                    break
        save_client_types_data(data)
