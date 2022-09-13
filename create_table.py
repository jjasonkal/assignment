from decouple import config
import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd
import io


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


def create_table_with_content(name, content):
    df = pd.DataFrame(content)
    df.head(0).to_sql(name, engine, if_exists='replace', index=False)  # drops old table and creates new empty table

    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, name)
    conn.commit()
