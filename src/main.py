from multiprocessing import Pool

# from joblib import Parallel, delayed

from infrastructure.database.postgres.data_types import BaseModel
from infrastructure.database.postgres.postgres_connection import DEFAULT_ENGIN
from stock_info.stock_indentifier.update_stocks import get_stock_info
from workers.market_watch import market_watch_worker
from workers.stock_info import stock_info_worker
from workers.stock_price import get_stock_price_worker


def worker_function(worker):
    return worker()


if __name__ == '__main__':
    # get_stock_info()
    # get_stock_price_worker()
    # market_watch_worker()
    BaseModel.metadata.create_all(DEFAULT_ENGIN)
    workers = [
        # stock_info_worker,
        # get_stock_info,
        market_watch_worker,
    ]

    with Pool(len(workers)) as p:
        results = p.map(worker_function, workers)
    # Parallel(n_jobs=len(workers))(delayed(worker)() for worker in workers)
