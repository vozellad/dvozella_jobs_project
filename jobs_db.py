import sqlite3


def open_db(filename):
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection):
    connection.commit()
    connection.close()
