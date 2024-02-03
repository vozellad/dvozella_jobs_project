"""Scrapes software developer job listings from Google Jobs in Boston, Massachusetts using serpapi, and saves the
results to a text file."""

from secrets import api_key
from serpapi import GoogleSearch
import jobs_db


def get_jobs_results(page):
    """Uses Serpapi to get a page of results from Google Jobs

    Keyword arguments:
    page -- Page of results to be returned. Starts at 0

    Returns:
    List of dictionaries containing information of job listings
    """

    # Get jobs data via Google query
    return GoogleSearch({
        "engine": "google_jobs",
        "q": "software developer",
        "location": "Boston,Massachusetts",
        "api_key": api_key,
        "start": page * 10  # 10 results per page. Every 10 results is start of page.
    }).get_dict()["jobs_results"]


def store_jobs_results(jobs_results):
    """Stores jobs results into text file

    Keyword arguments:
    jobs_results -- List of dictionaries containing job information

    Returns:
    None
    """

    with open(f"jobs_results.txt", "w+") as file:
        for j in jobs_results:
            file.write(str(j) + "\n")


def main():
    # Get jobs
    jobs_results = []
    for page in range(5):
        jobs_results += get_jobs_results(page)

    # Store jobs
    store_jobs_results(jobs_results)

    conn, cursor = jobs_db.open_db("jobs_db.sqlite")
    jobs_db.setup_db(cursor)
    jobs_db.insert_jobs(cursor, jobs_results)

    jobs_db.close_db(conn)


if __name__ == "__main__":
    main()
