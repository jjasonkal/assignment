from contextlib import contextmanager
from typing import List

import psycopg2

from .config import settings
from .models.weather import Weather, DistinctNames, AverageWeather, TopMetrics, MetricsColumns
from .queries.query_parser import query_parse


@contextmanager
def get_db_conn():
    with psycopg2.connect(settings.postgres_dsn) as conn:
        yield conn


def latest_weekly_forecast() -> List[Weather]:
    query = query_parse('app/queries/distinct_names.sql')

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            names = [DistinctNames.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in names:
                name = distinct.name
                query = query_parse('app/queries/latest_weekly_forecast.sql').format(name=name)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [Weather.parse_obj(dict(zip(columns, row))) for row in rows]
            return response


def last_hour_weekly_forecast() -> List[Weather]:
    query = query_parse('app/queries/distinct_names.sql')

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            names = [DistinctNames.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in names:
                name = distinct.name
                query = query_parse('app/queries/last_hour_weekly_forecast.sql')
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [Weather.parse_obj(dict(zip(columns, row))) for row in rows]
            return response


def average_of_last_3_forecasts() -> List[Weather]:
    query = query_parse('app/queries/distinct_names.sql')

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            names = [DistinctNames.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in names:
                name = distinct.name
                # TODO remove hardcoded average of metric columns
                query = query_parse('app/queries/average_of_last_3_forecasts.sql').format(name=name)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [AverageWeather.parse_obj(dict(zip(columns, row))) for row in rows]
            return response


def top_n_locations_of_each_metric(n) -> List[Weather]:
    # TODO give more generic expression for metric columns
    query = query_parse('app/queries/metric_column_names.sql')

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            metrics = [MetricsColumns.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in metrics:
                value = distinct.column_name
                query = query_parse('app/queries/top_n_locations_of_each_metric.sql').format(value=value, n=n)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[value] = [TopMetrics.parse_obj(dict(zip(columns, row))) for row in rows]
            return response
