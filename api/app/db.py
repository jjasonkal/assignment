from contextlib import contextmanager
from typing import List

import psycopg2

from .config import settings
from .models.weather import Weather, DistinctID, AverageWeather, TopMetrics, MetricsColumns
from .queries.query_parser import query_parse


def response_handling(response):
    if response:
        return response
    else:
        print(" Make sure that you have created the two tables and have filled them with some values ")
        return []


@contextmanager
def get_db_conn():
    with psycopg2.connect(settings.postgres_dsn) as conn:
        yield conn


def latest_weekly_forecast() -> List[Weather]:
    query = query_parse('app/queries/distinct_id.sql').format(table_cities='cities')

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            objects = [DistinctID.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in objects:
                city_id = distinct.id
                name = distinct.name
                query = query_parse('app/queries/latest_weekly_forecast.sql').format(city_id=city_id)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [Weather.parse_obj(dict(zip(columns, row))) for row in rows]

            try:
                return response_handling(response)
            except Exception as e:
                print(e)
                raise SystemExit(e)


def last_hour_weekly_forecast(test=False) -> List[Weather]:
    table_cities = 'cities'
    table_forecasts = 'forecasts'
    if test:
        table_cities = 'test_cities'
        table_forecasts = 'test_forecasts'
    query = query_parse('app/queries/distinct_id.sql').format(table_cities=table_cities)

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            objects = [DistinctID.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in objects:
                city_id = distinct.id
                name = distinct.name
                query = query_parse('app/queries/last_hour_weekly_forecast.sql').format(city_id=city_id,
                                                                                        table_forecasts=table_forecasts)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [Weather.parse_obj(dict(zip(columns, row))) for row in rows]

            try:
                return response_handling(response)
            except Exception as e:
                print(e)
                raise SystemExit(e)


def average_of_last_3_forecasts(test=False) -> List[Weather]:
    table_cities = 'cities'
    table_forecasts = 'forecasts'
    if test:
        table_cities = 'test_cities'
        table_forecasts = 'test_forecasts'
    query = query_parse('app/queries/distinct_id.sql').format(table_cities=table_cities)

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            objects = [DistinctID.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in objects:
                city_id = distinct.id
                name = distinct.name
                # TODO remove hardcoded average of metric columns
                query = query_parse('app/queries/average_of_last_3_forecasts.sql').format(city_id=city_id, table_forecasts=table_forecasts)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [AverageWeather.parse_obj(dict(zip(columns, row))) for row in rows]

            try:
                return response_handling(response)
            except Exception as e:
                print(e)
                raise SystemExit(e)


def top_n_locations_of_each_metric(n, test=False) -> List[Weather]:
    table_cities = 'cities'
    table_forecasts = 'forecasts'
    if test:
        table_cities = 'test_cities'
        table_forecasts = 'test_forecasts'
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
                query = query_parse('app/queries/top_n_locations_of_each_metric.sql').format(value=value, n=n, table_cities=table_cities, table_forecasts=table_forecasts)
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[value] = [TopMetrics.parse_obj(dict(zip(columns, row))) for row in rows]

            try:
                return response_handling(response)
            except Exception as e:
                print(e)
                raise SystemExit(e)
