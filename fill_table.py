from decouple import config
import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd
import io
from datetime import datetime

# get local variables from .env
dbname = config('DB_DATABASE')
host = config('DB_SERVER')
username = config('DB_USERNAME')
password = config('DB_PASSWORD')
psycopg = 'postgresql+psycopg2'
port = '5432'

engine = create_engine(F"{psycopg}://{username}:{password}@{host}:{port}/{dbname}")
conn = engine.raw_connection()
cur = conn.cursor()

connection = pg.connect(f"host={host} dbname={dbname} user={username} password={password}")


def fill_table_with_content(name, content):
    now = datetime.now()
    df = pd.DataFrame(content)
    df['name'] = name
    df['since'] = now
    table_name = 'forecasts'
    df.head(0).to_sql(table_name, engine, if_exists='append', index=False)

    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, table_name)
    conn.commit()
