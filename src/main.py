from multiprocessing.context import Process

from workers.stock_info import market_watch_worker

if __name__ == '__main__':
    workers = [
        market_watch_worker,
    ]

    processes = [Process(target=worker) for worker in workers]

    try:
        for process in processes:
            process.start()
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
