from typing import List

import requests

from stock_info.client_types.models import ClientTypeAllModel
from stock_info.client_types.save_data import save_client_types_data
from stock_info.urls import CLIENT_TYPE_ALL_URL, DEFAULT_HEADERS


class ClientType:
    def __init__(self):
        self.data: List[ClientTypeAllModel] = []
        self.__raw_data: str = ""
        self.__data = []

    def req(self, url):
        resp = requests.get(url, headers=DEFAULT_HEADERS)
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
        self.req(CLIENT_TYPE_ALL_URL)
        self.split_data()
        self.model_data()

    def save_data(self, last_changed_identifier: List[str] = None):
        if last_changed_identifier:
            data = [item for item in self.data if item.stock_id in last_changed_identifier]
        else:
            data = self.data

        save_client_types_data(data)
