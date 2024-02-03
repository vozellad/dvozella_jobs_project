import sqlite3


def open_db(filename):
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection):
    connection.commit()
    connection.close()


def setup_db(cursor):
    cursor.execute('''DROP TABLE IF EXISTS jobs;''')  # TEMP: testing code

    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
    job_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    company_name TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT NOT NULL
    );''')


def insert_jobs(cursor, jobs):
    column_names = ["job_id", "title", "company_name", "location", "description"]
    columns_str = ", ".join(column_names)
    placeholders_str = ", ".join("?" * len(column_names))
    sql_command = f'''INSERT OR IGNORE INTO jobs ({columns_str})
                      VALUES ({placeholders_str});'''

    for j in jobs:
        params = tuple(j[col] for col in column_names[:5])
        cursor.execute(sql_command, params)
