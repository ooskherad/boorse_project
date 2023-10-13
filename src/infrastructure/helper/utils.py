import datetime

import pytz

TEHRAN = pytz.timezone("Asia/Tehran")
UTC = pytz.UTC


def convert_string_to_time(str_time: str, d: datetime.date | None = None) -> datetime.datetime:
    le = len(str_time) - 1
    hour = int(str_time[:le - 3])
    minute = int(str_time[le - 3: le - 1])
    second = int(str_time[le - 1:])
    now = datetime.datetime.now() if not d else d
    return datetime.datetime(year=now.year, month=now.month, day=now.day, hour=hour, minute=minute, second=second)
