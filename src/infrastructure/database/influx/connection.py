from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS

from infrastructure import config


class InfluxDb:
    DEFAULT_BUCKET = ""
    influx_client: InfluxDBClient = None

    @classmethod
    def client(cls) -> InfluxDBClient:
        if cls.influx_client is None:
            cls.influx_client = InfluxDBClient(
                url=config.INFLUX_URL,
                token=config.INFLUX_TOKEN,
                org=config.INFLUX_ORG
            )
        return cls.influx_client

    @classmethod
    def write_api(cls):
        return cls.influx_client.write_api(
            write_options=ASYNCHRONOUS
        )
