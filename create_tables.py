from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
import psycopg2 as pg
from sqlalchemy import create_engine
import csv
from pathlib import Path

Base = declarative_base()

# get local variables from .env
dbname = config('DB_DATABASE')
host = config('DB_SERVER')
username = config('DB_USERNAME')
password = config('DB_PASSWORD')
psycopg = 'postgresql+psycopg2'
port = '5432'


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class Forecast(Base):
    __tablename__ = 'forecasts'
    date = Column(DateTime(30), primary_key=True)
    t_2m = Column(Float(5))
    absolute_humidity_2m = Column(Float(5))
    dew_point_2m = Column(Float(5))
    since = Column(DateTime(30), primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    cities = relationship(City)


class TestCity(Base):
    __tablename__ = 'test_cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class TestForecast(Base):
    __tablename__ = 'test_forecasts'
    date = Column(DateTime(30), primary_key=True)
    t_2m = Column(Float(5))
    absolute_humidity_2m = Column(Float(5))
    dew_point_2m = Column(Float(5))
    since = Column(DateTime(30), primary_key=True)
    city_id = Column(Integer, ForeignKey('test_cities.id'))
    cities = relationship(TestCity)


engine = create_engine(F"{psycopg}://{username}:{password}@{host}:{port}/{dbname}")

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine);

# Fill the test tables
engine = create_engine(F"{psycopg}://{username}:{password}@{host}:{port}/{dbname}")
conn = engine.raw_connection()
cur = conn.cursor()

connection = pg.connect(f"host={host} dbname={dbname} user={username} password={password}")

query = "DELETE FROM test_forecasts;"
cur.execute(query)
conn.commit()
query = "DELETE FROM test_cities;"
cur.execute(query)
conn.commit()
with open(Path(__file__).parent / 'csv/test_cities.csv', 'r') as f:
    reader = csv.reader(f)
    column_names = True
    for row in reader:
        if not column_names:
            query = f"INSERT INTO test_cities VALUES({row[0]},'{row[1]}');"
            cur.execute(query)
            conn.commit()
        column_names = False

with open(Path(__file__).parent / 'csv/test_forecasts.csv', 'r') as f:
    reader = csv.reader(f)
    column_names = True
    for row in reader:
        if not column_names:
            query = f"INSERT INTO test_forecasts VALUES(CAST('{row[0]}' AS timestamp),{float(row[1])},{float(row[2])},{float(row[3])},CAST('{row[4]}' AS timestamp),{int(row[5])});"
            cur.execute(query)
            conn.commit()
        column_names = False

cur.close()
