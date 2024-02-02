"""Scrapes software developer job listings from Google Jobs in Boston, Massachusetts using serpapi, and saves the
results to a text file."""

from secrets import api_key
from serpapi import GoogleSearch


def get_jobs_results(page_num):
    """Uses Serpapi to get a page of results from Google Jobs

    Keyword arguments:
    page-num -- Page of results to be returned

    Returns:
    List of dictionaries containing information of job listings
    """

    # 10 results per page. Every 10 results is start of page.
    page = (page_num - 1) * 10

    # Get dictionary of Google query
    search_results = GoogleSearch({
        "engine": "google_jobs",
        "q": "software developer",
        "location": "Boston,Massachusetts",
        # "api_key": api_key,
        "start": page
    }).get_dict()

    # Only get job data
    jobs_results = search_results["jobs_results"]

    return jobs_results


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
    # TEMP: commented out code to save tokens because we already have file of data

    # Get jobs
    # jobs_results = []
    # for page_num in range(1, 6):
    #    jobs_results += get_jobs_results(page_num)

    # Store jobs
    # store_jobs_results(jobs_results)

    pass


if __name__ == "__main__":
    main()
