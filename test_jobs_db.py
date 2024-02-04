import pytest
import jobs_db
import sqlite3


def test_jobs_db():
    db_connection = sqlite3.connect("test_jobs_db.sqlite")
    cursor = db_connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS jobs;''')
    jobs_db.setup_db(cursor)

    job = {
        "job_id": "asdf1234",
        "title": "Software Engineer Intern",
        "company_name": "Studious Studios",
        "location": "Austin, Indiana",
        "description": "Developing Applications",
        "detected_extensions": {"posted_at": "3 days ago", "salary": "10K–12K a year"},
        "related_links": [{"link": "google.com"}, {"link": "something.com"}],
        "job_highlights": [{"items": ["React", "Python"]}]
    }

    jobs_db.insert_jobs(cursor, [job])

    cursor.execute("SELECT * FROM jobs")
    fetch = cursor.fetchone()
    assert fetch is not None
    assert fetch[0] == "asdf1234"
    assert fetch[1] == "Software Engineer Intern"
    assert fetch[2] == "Studious Studios"
    assert fetch[3] == "Austin, Indiana"
    assert fetch[4] == "Developing Applications"
    assert fetch[5] == "3 days ago"
    assert fetch[6] == "10K–12K a year"

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
    print(fetch)
    assert fetch[0][2] == "React"
    assert fetch[1][2] == "Python"

    jobs_db.close_db(db_connection)
