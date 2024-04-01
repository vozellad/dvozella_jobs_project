"""Functions to filter job list for MainWindow objects"""

import re


def filter_keyword(jobs, keyword):
    """Search every job data fields to find whether they contain a string.

    Keyword arguments:
    jobs -- current state of filtered jobs from MainWindow object
    keyword -- text user inputted into "keyword" filter field

    Returns:
    jobs filtered based on keyword
    """

    return [j for j in jobs if keyword_in_job(keyword, j)]


def keyword_in_job(keyword, job):
    """Find keyword in job's sublists.

    Keyword arguments:
    keyword -- string to be found in job data
    job -- list to be searched through for keyword

    Returns:
    Boolean for if keyword is found
    """

    # First 7 items are just strings. Last two (links, qualifications) are lists of strings.
    return (keyword_in_list(keyword, job[:7]) or
            keyword_in_list(keyword, job[-2]) or
            keyword_in_list(keyword, job[-1]))


def keyword_in_list(keyword, l):
    """Searches list for keyword with null safety and case insensitivity.

    Keyword arguments:
    keyword -- string to be found in data
    l -- list of data to be searched for keyword

    Returns:
    Boolean for if keyword is found
    """

    if not l:
        return False
    return any(keyword.lower() in item.lower() for item in l)


def filter_city_location(jobs, user_city):
    """Filter jobs based on a city. User selects from available cities from jobs.

    Keyword arguments:
    jobs -- current state of filtered jobs from MainWindow object
    user_city -- city selected by user

    Returns:
    jobs filtered based on city
    """

    if not user_city:
        return
    return [j for j in jobs if j[3] and user_city == get_city_str(j[3])]


def get_city_str(city):
    """Formats a location like "Boston, MA" by removing text that isn't an address and removing the zipcode.

    Keyword arguments:
    city -- String of location

    Returns:
    city -- String of location formatted
    """

    city = remove_parenthesis_in_location(city)
    if re.search("[0-9-]+$", city):  # remove zipcode
        city = " ".join(city.split(" ")[:-1])
    return city


def remove_parenthesis_in_location(city):
    """Cuts out text that isn't location like "Boston, MA (+2 others)"

    Keyword arguments:
    city -- Location to format

    Returns:
    city -- Formatted location
    """

    if "(" in city:  # remove "(+# others)" occurrences
        city = re.findall(".+\(", city)[0][:-1].rstrip()
    return city


def get_city_locations(jobs):
    """Gathers cities of jobs.

    Keyword arguments:
    jobs -- current state of filtered jobs from MainWindow object

    Returns:
    An alphabetically sorted set of cities
    """

    cities = {get_city_str(j[3]) for j in jobs if j[3]}
    return sorted(cities)


def filter_remote(jobs, remote_checked):
    """Either filter to only get remote jobs or ignore the information.

    Keyword arguments:
    jobs -- current state of filtered jobs from MainWindow object
    remote_checked -- whether the user enabled remote jobs to be filtered

    Returns:
    Conditionally, list of remote jobs or None
    """

    if remote_checked:
        return [j for j in jobs if j[7]]
        # Way database works is it's either 1 or nothing.


def filter_min_salary(jobs, user_min_salary):
    """Filter jobs to only get what's at or above given yearly salary number.

    Keyword arguments:
    jobs -- current state of filtered jobs from MainWindow object
    user_min_salary -- user given number for minimum salary

    Returns:
    jobs filtered based on minimum salary
    """

    return [j for j in jobs if user_min_salary <= get_yearly_salary(j[6])]


def get_yearly_salary(salary):
    """Filter jobs to only get what's at or above given yearly salary number.

    Keyword arguments:
    salary -- String of salary

    Returns:
    new_salary -- Float of yearly salary
    """

    if not salary:
        return 0

    new_salary = re.findall("^[0-9K.]+", salary)[0]

    if new_salary[-1] == "K":
        new_salary = float(new_salary[:-1]) * 1000
    else:
        new_salary = float(new_salary)

    rate = salary.split()[-1]
    if rate.startswith("hour"):  # could be "hourly"
        new_salary *= 40 * 52
    elif rate.startswith("week"):
        new_salary *= 52

    return new_salary


def format_jobs_for_map(jobs):
    """Prepare job data for map.

    Keyword arguments:
    jobs -- list of jobs

    Returns:
    jobs_to_display -- formatted jobs for map: (id, title, company, formatted location)
    """

    jobs_to_display = []
    for j in jobs:
        location = remove_parenthesis_in_location(j[3])
        curr_data = tuple(j[:3]) + (location,)
        jobs_to_display.append(curr_data)
    return jobs_to_display
