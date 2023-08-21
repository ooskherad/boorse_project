from multiprocessing.context import Process

from infrastructure.database.postgres.data_types import BaseModel
from infrastructure.database.postgres.postgres_connection import DEFAULT_ENGIN
from workers.market_watch import market_watch_worker
from workers.stock_info import stock_info_worker

if __name__ == '__main__':
    BaseModel.metadata.create_all(DEFAULT_ENGIN)
    workers = [
        # stock_info_worker,
        market_watch_worker,
    ]

    processes = [Process(target=worker) for worker in workers]

    try:
        for process in processes:
            process.start()
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
