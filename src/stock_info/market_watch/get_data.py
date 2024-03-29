import datetime
from typing import List

import jdatetime
import requests as requests
from pydantic import BaseModel
from sqlalchemy import text

from database.models import Stock
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from infrastructure.helper.utils import TEHRAN, convert_string_to_time
from infrastructure.http_request import get
from stock_info.market_watch.models import MarketWatchModel
from stock_info.market_watch.save_data import save_market_watch_data
from stock_info.market_watch.utils import *
from stock_info.urls import INIT_MARKET_WATCH_URL, PLUS_MARKET_WATCH_URL


class MarketWatch:
    def __init__(self):
        self.duplicate_names = self.get_duplicate_names()
        self.data: List[MarketWatchModel] = []
        self.__raw_data: str = ""
        self.__data: any = None
        self.__heven_history = None
        self.__refer_history = None
        self.__heven = 0
        self.__refer = 0
        self.__len_data = 0
        self.date = None

    def req(self, url):
        resp = get(url)
        self.__raw_data = resp.text

    def split_data(self):
        data_ = self.__raw_data.split('@')
        try:
            if len(data_) < 2:
                self.__data = []
                return
            self.__data = data_[2].split(';')
            if data_[1] != '':
                split_date = data_[1].split(' ')[0].split('/')
                self.date = jdatetime.date(int('14' + split_date[0]), int(split_date[1]),
                                           int(split_date[2])).togregorian()
            self.__len_data = len(self.__data[0].split(','))
            self.calculate_refer()
        except Exception as e:
            print(e)

    def calculate_refer(self):
        self.__refer_history = self.__refer
        self.__refer = (int(self.__raw_data.split('@')[4]) // 25) * 25

    def calculate_heven(self, heven_in_data):
        if self.__heven < int(heven_in_data):
            self.__heven_history = self.__heven
            self.__heven = (int(heven_in_data) // 5) * 5

    def get_data_indices(self):
        if self.__len_data == 10:
            return UpdateReqIndices
        else:
            return FirstReqIndices

    def model_data(self):
        self.data.clear()
        row_indices = self.get_data_indices()
        for row_data in self.__data:
            sample = row_data.split(',')
            if sample[row_indices.STOCK_ID.value] in self.duplicate_names.keys():
                sample[row_indices.STOCK_ID.value] = self.duplicate_names[sample[row_indices.STOCK_ID.value]]
            market_watch_model = MarketWatchModel()
            for key, index in row_indices.__members__.items():
                key = key.lower()
                value = sample[index.value]
                if hasattr(market_watch_model, key):
                    if key == 'transaction_at':
                        value = convert_string_to_time(sample[index.value], self.date)
                        self.calculate_heven(sample[index.value])
                    if MarketWatchModel.__annotations__[key] == int:
                        value = int(float(value)) if value and value != '' else value
                    setattr(market_watch_model, key, value)
                else:
                    print()
            self.data.append(market_watch_model)
        return self.data

    def is_market_closed(self):
        if self.__heven == self.__heven_history \
                and self.__refer == self.__refer_history:
            return True
        return False

    def save_data(self):
        save_market_watch_data(self.data)

    def save_new_stocks(self):
        session = DEFAULT_SESSION_FACTORY()
        stocks_in_db = {}
        for stock in session.query(Stock).all():
            stocks_in_db[stock.id] = stock

        stock_ids = stocks_in_db.keys()
        for item in self.data:
            if item.stock_id not in stock_ids:
                stock_model = Stock()
                stock_model.id = item.stock_id
                stock_model.name_fa = item.name
                stock_model.symbol_name = item.symbol
                stock_model.industry_group_code = item.industry_group_code if item.industry_group_code != '' else None
                stock_model.eps = item.eps if item.eps != '' else None
                stock_model.total_stock_number = item.total_stock_number if item.total_stock_number != '' else None
                stock_model.base_volume = item.base_volume if item.base_volume != '' else None
                session.add(stock_model)
            else:
                pass
                # stock_model = stocks_in_db[item.stock_id]
                # stock_model.eps = item.eps if item.eps != '' else None
                # stock_model.total_stock_number = item.total_stock_number if item.total_stock_number != '' else None
                # stock_model.base_volume = item.base_volume if item.base_volume != '' else None

        session.commit()

    def get_data(self):
        url = INIT_MARKET_WATCH_URL if self.__heven == 0 and self.__refer == 0 else PLUS_MARKET_WATCH_URL
        self.req(url.format(h=self.__heven, r=self.__refer))
        self.split_data()
        self.model_data()

    def get_duplicate_names(self):
        session = DEFAULT_SESSION_FACTORY()
        query = """
        select s1.symbol_name
         , max(s1.id) filter ( where s1.name_en notnull ) as id
         , max(s1.id) filter ( where s1.name_en isnull) as fake_id
        from stocks s1
             join stocks s2 on s1.symbol_name = s2.symbol_name and s1.id <> s2.id
        group by s1.symbol_name, s2.symbol_name"""
        data = session.execute(text(query)).all()
        result = {}
        for item in data:
            result[str(item[2])] = item[1]
        return result
