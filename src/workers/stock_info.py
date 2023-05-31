import datetime

from stock_info.market_watch.get_data import MarketWatch
import time


def market_watch_worker():
    market_watch = MarketWatch()
    while True:
        if not _check_condition() or market_watch.is_market_closed():
            time.sleep(5)
            break
        try:
            market_watch.get_data()
            market_watch.save_data()
            time.sleep(2)
        except Exception as e:
            print(e)
            time.sleep(10)


def _check_condition():
    now = datetime.datetime.now()
    start_at = datetime.time(hour=9)
    end_at = datetime.time(hour=12, minute=30)
    if start_at < now.time() < end_at:
        return True
    return False


market_watch_worker()
