"""Functions to scrape software developer job listings from Google Jobs in Boston, Massachusetts using serpapi, and save
the results to a text file.
"""


from my_secrets import api_key
from serpapi import GoogleSearch


def get_jobs(page_amt):
    """Uses Serpapi to get results from Google Jobs

    Keyword arguments:
    page -- Amount of pages of results to be returned. Starts at 0

    Returns:
    List of dictionaries containing job listings
    """

    jobs = []
    for p in range(page_amt):
        jobs += GoogleSearch({
            "engine": "google_jobs",
            "q": "software developer",
            "location": "Boston,Massachusetts",
            "api_key": api_key,
            "start": page_amt * p  # 10 results per page. Every 10 results is start of page.
        }).get_dict()["jobs_results"]

    return jobs


def store_jobs(jobs):
    """Stores jobs results into text file

    Keyword arguments:
    jobs_results -- List of dictionaries containing job information

    Returns:
    None
    """

    with open(f"jobs_results.txt", "w+") as file:
        for j in jobs:
            file.write(str(j) + "\n")
