"""Gets job data and stores it in a database. Displays GUI to view job info."""

import jobs_db
import jobs_results
import jobs_excel
import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow


def get_job_data():
    """Gather jobs from Serpapi and Excel file, format the data for the database to take.

    Keyword arguments:
    None

    Returns:
    jobs -- Combination of results from Serpapi and records from Excel file
    """

    jobs = jobs_results.get_jobs(5)
    jobs_results.store_jobs(jobs)
    jobs = jobs_results.prepare_jobs_for_db(jobs)
    jobs += jobs_excel.get_jobs("Sprint3Data.xlsx")
    return jobs


def main():
    jobs = get_job_data()

    # Store job data
    conn, cursor = jobs_db.open_db("jobs_db.sqlite")
    jobs_db.setup_db(cursor)
    jobs_db.insert_jobs(cursor, jobs)

    # Get database records for GUI
    job_records = jobs_db.get_jobs(cursor)

    # Start GUI
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(lambda: jobs_db.close_db(conn))
    window = MainWindow(job_records)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
