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
        job_id = j["job_id"].strip()
        title = j["title"].strip()
        company_name = j["company_name"].strip()
        location = j.get("location", "").strip()
        description = j.get("description", "").strip()
        posted_at = j["detected_extensions"].get("posted_at", "").strip()
        salary = j["detected_extensions"].get("salary", "").strip()
        work_from_home = j["detected_extensions"].get("work_from_home", "")

        # If work_from_home empty but location has "anywhere", the job is considered remote1
        if work_from_home == "" and j["location"].strip().lower() == "anywhere":
            work_from_home = True

        benefits = get_highlights_section(j["job_highlights"], "Benefits")
        strip_str_in_list(benefits)

        # If salary wasn't in assigned location, it might be in another location
        if salary == "":
            min_salary, max_salary = get_salary(benefits, j["description"])
            salary = get_salary_format(min_salary, max_salary)

        # Get all links of current listing
        links = [d.get("link") for d in j["related_links"]]
        strip_str_in_list(links)

        qualifications = get_highlights_section(j["job_highlights"], "Qualifications")
        strip_str_in_list(qualifications)

        prepared_jobs += [(job_id, title, company_name, location, description, posted_at, salary,
                           work_from_home, links, qualifications)]

    return prepared_jobs


def get_highlights_section(highlights, title):
    """jobs_highlights has multiple indexed sets of items with titles. Titles are not guaranteed to stay in the same
    order. Searches for given title and returns items under that title.

    Keyword arguments:
    highlights -- The "job_highlights" section from the Serpapi data
    title -- The name the desired items are under

    Returns:
    Items associated with the given title. If no such title, returns empty string.
    """

    for section in highlights:
        if section.get("title") == title:
            return section.get("items")
    return ""


def get_salary(benefits: dict, job_description: str):
    """Looks for salary in multiple places.

    Keyword arguments:
    benefits -- Data from 'Benefits' section of Serpapi data
    job_description -- 'job_description" section of Serpapi data

    Returns:
    (min_salary, max_salary) -- Tuple of the salary range
    """

    # Code provided by professor with student modifications
    min_salary = 0
    max_salary = 0
    for item in benefits:
        if 'range' in item.lower():
            # from https://stackoverflow.com/questions/63714217/how-can-i-extract-numbers-containing-commas-from
            # -strings-in-python
            numbers = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', item)
            if numbers:  # if we found salary data, return it
                return float(numbers[0].replace(',', '')), float(numbers[1].replace(',', ''))
        numbers = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', item)
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
    """Gets salary range and forms a string.

    Keyword arguments:
    min_salary -- low end of salary range
    max_salary -- high end of salary range

    Returns:
    salary -- Worded version of salary range
    """
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


def strip_str_in_list(l):
    for i, s in enumerate(l):
        l[i] = s.strip()
