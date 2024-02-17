"""Gets Google job results via Serpapi and stores it in a database.
"""

import jobs_db
import jobs_results
import jobs_excel


def main():
    jobs = jobs_results.get_jobs(5)
    jobs_results.store_jobs(jobs)
    jobs = jobs_results.prepare_jobs_for_db(jobs)
    jobs += jobs_excel.get_jobs()

    conn, cursor = jobs_db.open_db("jobs_db.sqlite")
    jobs_db.setup_db(cursor)
    jobs_db.insert_jobs(cursor, jobs)

    jobs_db.close_db(conn)


if __name__ == "__main__":
    main()
