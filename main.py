"""Contains values to not be made publicly available on github."""
from secrets import api_key

"""Scrapes and parses Google search results"""
from serpapi import GoogleSearch


def get_jobs_results(page_num):
    # 10 results per page. Every 10 results is start of page.
    page = (page_num - 1) * 10

    # Get dictionary of Google query
    search_results = GoogleSearch({
        "engine": "google_jobs",
        "q": "software developer",
        "location": "Boston,Massachusetts",
        "api_key": api_key,
        "start": page
    }).get_dict()

    # Only get job data
    jobs_results = search_results["jobs_results"]

    return jobs_results


def store_jobs_results(jobs_results):
    with open(f"jobs_results.txt", "w+") as file:
        for j in jobs_results:
            file.write(str(j) + "\n")


def main():
    # Get jobs
    jobs_results = []
    for page_num in range(1, 6):
        jobs_results += get_jobs_results(page_num)

    # Store jobs
    store_jobs_results(jobs_results)


if __name__ == "__main__":
    main()
