import sqlite3


def open_db(filename):
    """Open a connection to a(n) SQLite database file and return the database connection and cursor.

    Keyword arguments:
    filename -- The name of the database file to connect to.

    Returns:
    A tuple of the database connection and cursor.
    """

    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection):
    connection.commit()
    connection.close()


def setup_db(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
    job_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    company_name TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT NOT NULL,
    posted_at TEXT NOT NULL,
    salary TEXT DEFAULT ""
    );''')

    cursor.execute('''CREATE TABLE related_links (
    link_id INTEGER PRIMARY KEY,
    job_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    );''')

    cursor.execute('''CREATE TABLE qualifications (
    qualification_id INTEGER PRIMARY KEY,
    job_id INTEGER NOT NULL,
    qualification TEXT NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    );''')


def insert_jobs(cursor, jobs):
    column_names = ["job_id", "title", "company_name", "location", "description", "posted_at", "salary"]
    columns_str = ", ".join(column_names)
    placeholders_str = ", ".join("?" * len(column_names))
    sql_command = f'''INSERT OR IGNORE INTO jobs ({columns_str})
                      VALUES ({placeholders_str});'''

    for j in jobs:
        posted_at = j["detected_extensions"].get("posted_at", "")
        salary = j["detected_extensions"].get("salary", "")
        params = tuple(j[col] for col in column_names[:5]) + (posted_at, salary)
        cursor.execute(sql_command, params)

        links = [d["link"] for d in j["related_links"]]
        for link in links:
            cursor.execute('''INSERT INTO related_links (job_id, url)
                              VALUES (?, ?);''', (j["job_id"], link))

        qualifications = j["job_highlights"][0].get("items")
        for q in qualifications:
            cursor.execute('''INSERT INTO qualifications (job_id, qualification)
                              VALUES (?, ?)''', (j["job_id"], q))
