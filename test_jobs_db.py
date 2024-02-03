import pytest
import jobs_db
import sqlite3


def test_setup_db():
    db_connection = sqlite3.connect("test_jobs_db.sqlite")
    cursor = db_connection.cursor()

    jobs_db.setup_db(cursor)
