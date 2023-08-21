from typing import List

from databse.models import Index as IndexModel, IndexStock, Stock
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from stock_info.stock_index.models import Index


def save_stock_indices_data(data: List[Index]):
    save_in_postgres(data)


def save_in_postgres(data: List[Index]):
    session = DEFAULT_SESSION_FACTORY()
    session2 = DEFAULT_SESSION_FACTORY()
    stocks_in_db = [stock.id for stock in session.query(Stock.id).all()]
    indices_in_db = [index.id for index in session.query(IndexModel.id).all()]
    index_stocks_ind_db = [str(r.stock_id) + str(r.index_id) for r in session.query(IndexStock).all()]

    new_stock_ids = []
    new_index_ids = []
    new_index_stocks = []
    for index in data:
        if int(index.identifier) not in indices_in_db and index.identifier not in new_index_ids:
            index_model = IndexModel()
            index_model.id = index.identifier
            index_model.name = index.name
            new_index_ids.append(index.identifier)
            session.add(index_model)
        for stock in index.stocks:
            if int(stock.identifier) not in stocks_in_db and stock.identifier not in new_stock_ids:
                stock_model = Stock()
                stock_model.name_fa = stock.name_fa
                stock_model.id = stock.identifier
                new_stock_ids.append(stock.identifier)
                session.add(stock_model)

            r = str(index.identifier) + str(stock.identifier)
            if r not in index_stocks_ind_db and r not in new_index_stocks:
                stock_index = IndexStock()
                stock_index.stock_id = stock.identifier
                stock_index.index_id = index.identifier
                new_index_stocks.append(r)
                session2.add(stock_index)

    session.commit()
    session2.commit()
