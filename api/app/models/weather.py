from datetime import datetime
from pydantic import BaseModel


class Metrics(BaseModel):
    t_2m: float
    absolute_humidity_2m: float
    dew_point_2m: float


class Weather(Metrics):
    date: datetime
    since: datetime


class DistinctID(BaseModel):
    id: int
    name: str


class MetricsColumns(BaseModel):
    column_name: str


class AverageWeather(Metrics):
    date: datetime


class TopMetrics(BaseModel):
    name: str
    maximum: float
