TSE_URL = 'http://www.tsetmc.com/'
INIT_MARKET_WATCH_URL = "http://old.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h={h}&r={r}"
PLUS_MARKET_WATCH_URL = "http://old.tsetmc.com/tsev2/data/MarketWatchPlus.aspx?h={h}&r={r}"
CLIENT_TYPE_ALL_URL = "http://old.tsetmc.com/tsev2/data/ClientTypeAll.aspx"
MARKET_INDICES = "http://cdn.tsetmc.com/api/Index/GetIndexB1LastAll/All/{market}"
INDEX_STOCKS = "http://cdn.tsetmc.com/api/ClosingPrice/GetIndexCompany/{index_id}"
STOCK_IDENTIFIER = "http://cdn.tsetmc.com/api/Instrument/GetInstrumentIdentity/{stock_id}"

DEFAULT_HEADERS = {
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
}
