from enum import Enum


class FirstReqIndices(Enum):
    STOCK_ID = 0
    SYMBOL = 2
    NAME = 3
    TRANSACTION_AT = 4
    PRICE_FIRST = 5
    PRICE_CLOSE = 6
    PRICE_LAST = 7
    TRANSACTION_COUNT = 8
    TRANSACTION_VOLUME = 9
    PRICE_MIN = 11
    PRICE_MAX = 12
    PRICE_YESTERDAY = 13
    EPS = 14
    PRICE_AUTHORIZED_MAX = 19
    PRICE_AUTHORIZED_MIN = 20
    TOTAL_STOCK_NUMBER = 21


class UpdateReqIndices(Enum):
    STOCK_ID = 0
    TRANSACTION_AT = 1
    PRICE_FIRST = 2
    PRICE_CLOSE = 3
    PRICE_LAST = 4
    TRANSACTION_COUNT = 5
    TRANSACTION_VOLUME = 6
    PRICE_MIN = 8
    PRICE_MAX = 9
