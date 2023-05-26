import time
from datetime import datetime
from typing import List

import requests as requests

from infrastructure.helper.utils import TEHRAN
from stock_info.market_watch.models import MarketWatchModel
from stock_info.market_watch.save_data import save_market_watch_data
from stock_info.market_watch.utils import *
from stock_info.urls import MARKET_WATCH_URL


class MarketWatch:
    def __init__(self):
        self.data: List[MarketWatchModel] = []
        self.__raw_data: str = ""
        self.__data: any = None
        self.__heven_history = None
        self.__refer_history = None
        self.__heven = 0
        self.__refer = 0
        self.__len_data = 0

    def req(self, url):
        resp = requests.get(url)
        self.__raw_data = resp.text

    def split_data(self):
        data_ = self.__raw_data.split('@')
        self.__data = data_[2].split(';')
        self.__len_data = len(self.__data[0].split(','))

    def calculate_refer(self):
        self.__refer_history = self.__refer
        self.__refer = (int(self.__raw_data.split('@')[4]) // 25) * 25

    def calculate_heven(self, heven_in_data):
        if self.__heven < int(heven_in_data):
            self.__heven_history = self.__heven
            self.__heven = (int(heven_in_data) // 5) * 5

    def get_data_indices(self):
        if self.__len_data == 10:
            return UpdateReqIndices()
        else:
            return FirstReqIndices()

    def model_data(self):
        self.data.clear()
        row_indices = self.get_data_indices()
        for row_data in self.__data:
            sample = row_data.split(',')

            self.calculate_heven(sample[row_indices.heven])

            market_watch_model = MarketWatchModel(stock_id=sample[row_indices.identifier.id],
                                                  price=sample[row_indices.fields.last_price],
                                                  volume=sample[row_indices.fields.volume])
            self.data.append(market_watch_model)
        return self.data

    @staticmethod
    def check_time(
            hour: int,
            minute: int = 0,
            second: int = 0,
            microsecond: int = 0
    ):
        now = datetime.now(TEHRAN)
        specific_time = datetime.now(TEHRAN).replace(
            hour=hour, minute=minute,
            second=second, microsecond=microsecond
        )
        if now > specific_time:
            return True
        else:
            return False

    def is_market_closed(self):
        if self.__heven == self.__heven_history \
                and self.__refer == self.__refer_history:
            return True
        return False

    def start(self, base_url):
        while True:
            # check for expiration of market time
            # if self.check_time(hour=13, minute=30):
            #     break

            # send request
            url = base_url.format(h=self.__heven, r=self.__refer)
            self.req(url)
            # split string data to list per each symbol
            self.split_data()
            self.calculate_refer()
            # packing data for send to infulxdb
            insert_data = self.model_data()

            # sleep time
            time.sleep(1)

    def main(self):
        while True:
            # check for market is closed
            # check for start market time (h=10, because time zone not true)
            # correct market start time is 9:00 am
            try:
                print('start project....')
                # if self.check_time(hour=10) \
                #         and not self.is_market_closed():
                self.start(MARKET_WATCH_URL)
                time.sleep(10)
                break
            except Exception as e:
                print(e)
                time.sleep(20)
                pass

    def save_data(self):
        save_market_watch_data(self.data)

    def get_data(self):
        self.req(MARKET_WATCH_URL.format(h=self.__heven, r=self.__refer))
        self.split_data()
        self.calculate_refer()
        self.model_data()
