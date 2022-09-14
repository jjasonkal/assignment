from contextlib import contextmanager
from typing import List

import psycopg2

from .config import settings
from .models.weather import Weather, DistinctNames, AverageWeather, TopMetrics, MetricsColumns


@contextmanager
def get_db_conn():
    with psycopg2.connect(settings.postgres_dsn) as conn:
        yield conn


def latest_weekly_forecast() -> List[Weather]:
    query = f"SELECT DISTINCT name FROM forecasts where DATE(date) >= DATE(NOW());"

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            names = [DistinctNames.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in names:
                name = distinct.name
                query = f"select * from forecasts where name = '{name}' and " \
                        f"since = (select distinct  since from " \
                        f"forecasts where name = '{name}' order by since desc limit 1)" \
                        f"and DATE(date) >= DATE(NOW())"
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [Weather.parse_obj(dict(zip(columns, row))) for row in rows]
            return response


def last_hour_weekly_forecast() -> List[Weather]:
    query = f"SELECT DISTINCT name FROM forecasts where DATE(date) >= DATE(NOW());"

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            names = [DistinctNames.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in names:
                name = distinct.name
                query = f"WITH ranked_messages AS (SELECT m.*, ROW_NUMBER() OVER (PARTITION BY DATE(date) ORDER BY " \
                        f"date DESC) AS rn FROM forecasts AS m) SELECT * FROM ranked_messages WHERE rn = 1 and DATE(" \
                        f"date) >= DATE(NOW())" \
                        f"ORDER BY date; "
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [Weather.parse_obj(dict(zip(columns, row))) for row in rows]
            return response


def average_of_last_3_forecasts() -> List[Weather]:
    query = f"SELECT DISTINCT name FROM forecasts where DATE(date) >= DATE(NOW());"

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            names = [DistinctNames.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in names:
                name = distinct.name
                query = f"select date, avg(t_2m) as t_2m, avg(dew_point_2m) as dew_point_2m, " \
                        f"avg(absolute_humidity_2m) as absolute_humidity_2m from forecasts  where name = '{name}' " \
                        f"and since in" \
                        f" (select distinct since from forecasts where name = '{name}' order by since desc limit 3) and" \
                        f" DATE(date) >= DATE(NOW())" \
                        f"group by " \
                        f"forecasts.date, forecasts.name order by date; "
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[name] = [AverageWeather.parse_obj(dict(zip(columns, row))) for row in rows]
            return response


def top_n_locations_of_each_metric(n) -> List[Weather]:
    query = f"SELECT column_name FROM INFORMATION_SCHEMA.columns WHERE TABLE_NAME = N'forecasts' and column_name " \
            f"like('%2m') "

    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            metrics = [MetricsColumns.parse_obj(dict(zip(columns, row))) for row in rows]

            response = {}
            for distinct in metrics:
                value = distinct.column_name
                query = f"Select name, max({value}) as maximum From  forecasts where DATE(date) >= DATE(NOW()) Group " \
                        f"By name " \
                        f"order by max({value}) desc limit {n}; "
                cursor.execute(query)
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                response[value] = [TopMetrics.parse_obj(dict(zip(columns, row))) for row in rows]
            return response
