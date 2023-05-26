
class FirstReqIndices:
    identifier = type("identifier", (), {
        "id": 0,
        "name": 3,
        "symbol": 2,
    })
    fields = type("fields", (), {
        "volume": 9,
        "last_price": 7,
    })
    heven = 4


class UpdateReqIndices:
    identifier = type("identifier", (), {
        "id": 0,
    })
    fields = type("fields", (), {
        "volume": 6,
        "last_price": 4,
    })
    heven = 1
