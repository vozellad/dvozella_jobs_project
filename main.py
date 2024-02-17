"""Gets Google job results via Serpapi and stores it in a database.
"""

import jobs_db
import jobs_results


def main():
    # Get jobs
    jobs = []
    for page in range(5):
        jobs += jobs_results.get_jobs(page)
    # Write jobs to file
    jobs_results.store_jobs(jobs)

    conn, cursor = jobs_db.open_db("jobs_db.sqlite")
    jobs_db.setup_db(cursor)
    jobs_db.insert_jobs(cursor, jobs)
    jobs_db.close_db(conn)


if __name__ == "__main__":
    main()
