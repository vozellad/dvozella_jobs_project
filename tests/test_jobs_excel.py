"""Testing functions in test_jobs_results.py."""

import pytest
import jobs_excel
import jobs_db
import sqlite3


def test_get_jobs(excel_file_path):
    """Tests if records from Excel file are retrieved correctly.
    Tests to make sure data goes into table.
    """

    jobs = jobs_excel.get_jobs(excel_file_path)

    assert len(jobs) == 750

    db_connection = sqlite3.connect("test_jobs_db.sqlite")
    cursor = db_connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS jobs;''')
    cursor.execute('''DROP TABLE IF EXISTS related_links;''')
    cursor.execute('''DROP TABLE IF EXISTS qualifications;''')
    jobs_db.setup_db(cursor)

    jobs_db.insert_jobs(cursor, jobs)

    # Make salary string
    if jobs[0][7] == jobs[0][6]:
        salary = str(jobs[0][7])
    else:
        salary = f"{jobs[0][7]} - {jobs[0][6]}"
    if jobs[0][8] != "N/A":
        salary += f" {jobs[0][8]}"

    # Confirm data from Excel file is correctly inserted into db table
    cursor.execute("SELECT * FROM jobs")
    fetch = cursor.fetchone()
    assert fetch is not None
    assert fetch[0] == jobs[0][0]
    assert fetch[1] == jobs[0][1]
    assert fetch[2] == jobs[0][2]
    assert fetch[3] == jobs[0][3]
    assert fetch[4] == ""
    assert fetch[5] == jobs[0][5]
    assert fetch[6] == jobs[0][6]
    assert fetch[7] == ""

    jobs_db.close_db(db_connection)