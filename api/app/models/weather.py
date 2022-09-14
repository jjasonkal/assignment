from datetime import datetime
from pydantic import BaseModel


class Metrics(BaseModel):
    t_2m: float
    absolute_humidity_2m: float
    dew_point_2m: float


class Weather(Metrics):
    date: str
    since: datetime


class DistinctNames(BaseModel):
    name: str


class MetricsColumns(BaseModel):
    column_name: str


class AverageWeather(Metrics):
    date: str


class TopMetrics(BaseModel):
    name: str
    maximum: float
