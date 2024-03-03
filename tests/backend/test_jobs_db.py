"""Testing functions in jobs_db.py."""

import pytest
import jobs_db
import sqlite3


def test_jobs_db():
    """Tests the entire process of handling database for jobs.
    Testing includes creating, updating, and deleting jobs data.
    """

    db_connection = sqlite3.connect("../test_jobs_db.sqlite")
    cursor = db_connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS jobs;''')
    cursor.execute('''DROP TABLE IF EXISTS related_links;''')
    cursor.execute('''DROP TABLE IF EXISTS qualifications;''')
    jobs_db.setup_db(cursor)

    job = ("asdf1234", "Software Engineer Intern", "Studious Studios", "Austin, Indiana", "Developing Applications",
           "3 days ago", "10K-12K a year", True, ["google.com", "something.com"], ["React", "Python"])

    jobs_db.insert_jobs(cursor, [job])

    # Get and confirm data in tables are accurately inserted

    cursor.execute("SELECT * FROM jobs")
    fetch = cursor.fetchone()
    assert fetch is not None
    assert fetch[0] == "asdf1234"
    assert fetch[1] == "Software Engineer Intern"
    assert fetch[2] == "Studious Studios"
    assert fetch[3] == "Austin, Indiana"
    assert fetch[4] == "Developing Applications"
    assert fetch[5] == "3 days ago"
    assert fetch[6] == "10K-12K a year"
    assert fetch[7] == True

    cursor.execute("SELECT * FROM related_links")
    fetch = cursor.fetchall()
    assert fetch is not None
    assert fetch[0][2] == "google.com"
    assert fetch[1][2] == "something.com"

    cursor.execute("SELECT * FROM qualifications")
    fetch = cursor.fetchall()
    assert fetch is not None
    assert fetch[0] is not None
    assert fetch[1] is not None
    assert fetch[0][2] == "React"
    assert fetch[1][2] == "Python"

    jobs_db.close_db(db_connection)
