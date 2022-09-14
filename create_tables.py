from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from decouple import config

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
    name = Column(String(250), nullable=False)


class Forecast(Base):
    __tablename__ = 'forecasts'
    date = Column(DateTime(30), primary_key=True)
    t_2m = Column(Float(5))
    absolute_humidity_2m = Column(Float(5))
    dew_point_2m = Column(Float(5))
    since = Column(DateTime(30), primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    cities = relationship(City)


engine = create_engine(F"{psycopg}://{username}:{password}@{host}:{port}/{dbname}")

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine);
