from typing import List

from stock_info.client_types.models import ClientTypeAllModel


def save_client_types_data(data: List[ClientTypeAllModel]):
    save_in_postgres(data)


def save_in_postgres(data: List[ClientTypeAllModel]):
    pass
