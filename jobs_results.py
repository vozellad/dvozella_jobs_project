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


def prepare_jobs_for_db(jobs):
    """Based on the structure of data given by Serpapi, get the relevant data and return it for it to be used in the
    database. Serpapi data structure is a list of dictionaries with each dict being a job.

    Keyword arguments:
    jobs -- List of dictionaries with each dict being a job

    Returns:
    prepared_jobs -- List of tuples of jobs with data structured for database
    """

    prepared_jobs = []

    for j in jobs:
        # Get SQL data parameters for new table row
        job_id = j["job_id"]
        title = j["title"]
        company_name = j["company_name"]
        location = j.get("location", "")
        description = j.get("description", "")
        posted_at = j["detected_extensions"].get("posted_at", "")
        salary = j["detected_extensions"].get("salary", "")
        work_from_home = j["detected_extensions"].get("work_from_home", "")

        # If work_from_home empty but location has "anywhere", the job is considered remote
        if work_from_home == "" and j["location"].strip().lower() == "anywhere":
            work_from_home = True

        # Get all links of current listing
        links = [d.get("link") for d in j["related_links"]]

        # Get all qualifications of current listing
        qualifications = j["job_highlights"][0].get("items")

        prepared_jobs += [(job_id, title, company_name, location, description, posted_at, salary,
                          work_from_home, links, qualifications)]

    return prepared_jobs

