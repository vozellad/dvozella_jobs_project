"""Module for handling database for jobs. Includes creating, updating, and deleting jobs data."""


import sqlite3


def open_db(filename):
    """Open a connection to a(n) SQLite database file and return the database connection and cursor.

    Keyword arguments:
    filename -- The name of the database file to connect to

    Returns:
    A tuple of the database connection and cursor
    """

    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection):
    """Commit any pending transaction to the database and close the connection.

    Keyword arguments:
    connection -- Database connection object to be closed

    Returns:
    None
    """

    connection.commit()
    connection.close()


def setup_db(cursor):
    """
    Create 3 tables in the database.
    First called 'jobs' is the main table meant to store data of each listing.
    Second table called 'related_links' is itself a piece of data for the first table but meant to store multiple links
    for each listing.
    Third table called 'qualifications' is similar to the second table but stores the multiple qualifications instead of
    links.

    Keyword arguments:
    cursor -- Used to execute SQL code to create tables

    Returns:
    None
    """

    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
    job_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    company_name TEXT NOT NULL,
    location TEXT DEFAULT "",
    description TEXT DEFAULT "",
    posted_at TEXT DEFAULT "",
    salary TEXT DEFAULT "",
    remote BOOLEAN DEFAULT FALSE
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS related_links (
    link_id INTEGER PRIMARY KEY,
    job_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS qualifications (
    qualification_id INTEGER PRIMARY KEY,
    job_id INTEGER NOT NULL,
    qualification TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    );''')


def __insert_job(cursor, job):
    """Insert given data into database.
    Data in jobs must be ordered correctly. If no data for something, give it empty value.

    Keyword arguments:
    cursor -- Used to insert values into the appropriate tables
    job -- Tuples of job
            Order of data: (job_id, title, company_name, location, description, posted_at, salary,
                            remote, links, qualifications)

    Returns:
    None
    """

    # Create string of SQL command used to insert new row into jobs table
    column_names = ["job_id", "title", "company_name", "location", "description", "posted_at", "salary", "remote"]
    columns_str = ", ".join(column_names)
    placeholders_str = ", ".join("?" * len(column_names))
    sql_command = f'''INSERT OR IGNORE INTO jobs ({columns_str})
                      VALUES ({placeholders_str});'''

    cursor.execute(sql_command, job[:8])

    # Insert every link individually into related_links table
    links = job[8]
    for link in links:
        cursor.execute('''INSERT OR IGNORE INTO related_links (job_id, url)
                                  VALUES (?, ?);''', (job[0], link))

    # Insert every qualification individually into qualifications table
    qualifications = job[9]
    for q in qualifications:
        cursor.execute('''INSERT OR IGNORE INTO qualifications (job_id, qualification)
                                  VALUES (?, ?)''', (job[0], q))


def insert_jobs(cursor, jobs):
    """Insert given data into database.
    Data in jobs must be ordered correctly. If no data for something, give it empty value.
    Uses _insert_jobs() to catch exceptions.

    Keyword arguments:
    cursor -- Used to insert values into the appropriate tables
    jobs -- List of tuples of jobs
            Order of data: (job_id, title, company_name, location, description, posted_at, salary,
                            remote, links, qualifications)

    Returns:
    None
    """

    for j in jobs:
        try:
            __insert_job(cursor, j)
        except sqlite3.IntegrityError:
            print(f"Error inserting job {j[0]}. It's already there.")
        except sqlite3.OperationalError as e:
            print(f"Error inserting job {e}.")


def get_jobs(cursor):
    cursor.execute("SELECT * FROM jobs")
    return cursor.fetchall()
