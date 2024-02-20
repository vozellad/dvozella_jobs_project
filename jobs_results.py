"""Module for handling Serpapi data."""

from my_secrets import api_key
from serpapi import GoogleSearch
import re


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

        # If work_from_home empty but location has "anywhere", the job is considered remote1
        if work_from_home == "" and j["location"].strip().lower() == "anywhere":
            work_from_home = True

        benefits = get_highlights_section(j["job_highlights"], "Benefits")

        # If salary wasn't in assigned location, it might be in another location
        if salary == "":
            min_salary, max_salary = get_salary(benefits, j["description"])
            salary = get_salary_format(min_salary, max_salary)

        # Get all links of current listing
        links = [d.get("link") for d in j["related_links"]]

        qualifications = get_highlights_section(j["job_highlights"], "Qualifications")

        prepared_jobs += [(job_id, title, company_name, location, description, posted_at, salary,
                           work_from_home, links, qualifications)]

    return prepared_jobs


def get_highlights_section(highlights, title):
    for section in highlights:
        if section.get("title") == title:
            return section
    return ""


def get_salary(benefits_section: dict, job_description: str):
    """Looks for salary in multiple places."""
    # Code provided by professor
    min_salary = 0
    max_salary = 0
    if benefits_section:  # if we got a dictionary with stuff in it
        for benefit_item in benefits_section['items']:
            if 'range' in benefit_item.lower():
                # from https://stackoverflow.com/questions/63714217/how-can-i-extract-numbers-containing-commas-from
                # -strings-in-python
                numbers = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', benefit_item)
                if numbers:  # if we found salary data, return it
                    return float(numbers[0].replace(',', '')), float(numbers[1].replace(',', ''))
            numbers = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', benefit_item)
            if len(numbers) == 2 and int(
                    # some jobs just put the numbers in one item and the description in another
                    numbers[0].replace(',', '')) > 30:
                return float(numbers[0].replace(',', '')), float(numbers[1].replace(',', ''))
            else:
                return min_salary, max_salary
    location = job_description.find("salary range")
    if location < 0:
        location = job_description.find("pay range")
    if location < 0:
        return min_salary, max_salary
    numbers = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', job_description[location:location + 50])
    if numbers:
        return float(numbers[0].replace(',', '')), float(numbers[1].replace(',', ''))
    return min_salary, max_salary


def get_salary_format(min_salary, max_salary):
    if min_salary == max_salary:
        salary = str(min_salary)
    else:
        salary = f"{min_salary} - {max_salary}"

    salary_time_period = 'N/A'
    if 0 < min_salary < 900:
        salary_time_period = 'Hourly'
    elif min_salary > 0:
        salary_time_period = "Yearly"

    if salary_time_period != "N/A":
        salary += f" {salary_time_period}"
    return salary
