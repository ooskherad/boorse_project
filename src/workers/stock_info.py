import datetime


import time

from stock_info.stock_index.get_data import StockIndex


def stock_info_worker():
    a = StockIndex()
    while True:
        if not _check_condition():
            time.sleep(5)
            break
        try:
            a.get_data()
            a.save_data()
        except Exception as e:
            print(e)
            time.sleep(10)


def _check_condition():
    return True
    now = datetime.datetime.now()
    start_at = datetime.time(hour=8, minute=59)
    end_at = datetime.time(hour=12, minute=31)
    if start_at < now.time() < end_at:
        return True
    return False

