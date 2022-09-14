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
    df = pd.DataFrame()

    query = f"SELECT id FROM cities where name = '{name}'"
    cursor = conn.cursor()
    city_id = 0
    try:
        cursor.execute(query)
        conn.commit()
        rows = cursor.fetchall()
        if rows:
            city_id = rows[0][0]
        else:
            query = f"SELECT max(id) FROM cities"
            cursor.execute(query)
            conn.commit()
            rows = cursor.fetchall()
            if rows != [(None,)]:
                city_id = rows[0][0] + 1
            query = "INSERT INTO cities VALUES(%d,'%s');" % (city_id, name)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
    except (Exception, pg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()

    # df['date'] = now
    df['date'] = [datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ') for x in
                  content[0]['coordinates'][0]['dates']]
    for metric in content:
        df[metric['parameter'].split(':')[0]] = [x['value'] for x in metric['coordinates'][0]['dates']]
    df['since'] = now
    df['city_id'] = city_id
    table_name = 'forecasts'
    df.head(0).to_sql(table_name, engine, if_exists='append', index=False)

    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, table_name)
    conn.commit()
