import json

import requests

from databse.models import Stock
from infrastructure.database.postgres.postgres_connection import DEFAULT_SESSION_FACTORY
from stock_info.urls import STOCK_IDENTIFIER
from infrastructure.http_request import DEFAULT_HEADERS


# {'instrumentIdentity': {'sector': {'dEven': 0, 'cSecVal': '01 ', 'lSecVal': 'زراعت و خدمات وابسته'}, 'subSector': {'dEven': 0, 'cSecVal': None, 'cSoSecVal': 121, 'lSoSecVal': 'كشاورزي، دامپروري و خدمات وابسته'}, 'cValMne': 'ZPRS1', 'lVal18': 'Pars Agro.', 'cSocCSAC': 'ZPRS', 'lSoc30': 'ملي كشت و صنعت و دامپروري پارس', 'yMarNSC': 'NO', 'yVal': '300', 'insCode': '0', 'lVal30': 'ملي كشت و صنعت و دامپروري پارس', 'lVal18AFC': 'زپارس', 'flow': 0, 'cIsin': 'IRO1ZPRS0001', 'zTitad': 0.0, 'baseVol': 0, 'instrumentID': 'IRO1ZPRS0001', 'cgrValCot': 'N2', 'cComVal': '5', 'lastDate': 0, 'sourceID': 0, 'flowTitle': '', 'cgrValCotTitle': 'بازار دوم بورس'}}

def get_stock_info():
    session = DEFAULT_SESSION_FACTORY()
    stocks = session.query(Stock).all()
    for stock in stocks:
        resp = requests.get(STOCK_IDENTIFIER.format(stock_id=stock.id), headers=DEFAULT_HEADERS)
        raw_data = resp.text
        data = json.loads(raw_data)

        stock.market = data['instrumentIdentity']['cgrValCotTitle']
        stock.symbol_name = data['instrumentIdentity']['lVal18AFC']
        stock.base_volume = data['instrumentIdentity']['baseVol']
        stock.table_code = data['instrumentIdentity']['cComVal']
        stock.name_fa = data['instrumentIdentity']['lSoc30']
        stock.company_digit4 = data['instrumentIdentity']['cSocCSAC']
        stock.company_digit_code12 = data['instrumentIdentity']['cIsin']
        stock.industry_group_code = data['instrumentIdentity']['sector']['cSecVal']
        stock.industry_group_name = data['instrumentIdentity']['sector']['lSecVal']
        stock.industry_subgroup_code = data['instrumentIdentity']['subSector']['cSoSecVal']
        stock.industry_subgroup_name = data['instrumentIdentity']['subSector']['lSoSecVal']
        stock.name_en = data['instrumentIdentity']['lVal18']
        stock.symbol_digit_code12 = data['instrumentIdentity']['instrumentID']
        stock.symbol_digit5 = data['instrumentIdentity']['cValMne']
        stock.symbol_name_30 = data['instrumentIdentity']['lVal30']
        stock.creation_data = data
    session.commit()


get_stock_info()
