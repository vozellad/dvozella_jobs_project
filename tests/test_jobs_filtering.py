"""Testing filter functions in jobs_filtering.py that are used in mainwindow.py"""

import pytest

import jobs_filtering


@pytest.fixture
def jobs():
    return [
        ["1", "Software Engineer", "ABC Inc.", "New York", "Job description...", "2024-03-01", "100K - 120K",
         True, [], []],
        ["2", "Data Scientist", "XYZ Corp.", "San Francisco", "Job description...", "2024-03-02", "60 hourly",
         False, [], []],
        ["3", "Product Manager", "123 Co.", "New York", "Job description...", "2024-03-03", "150000 - 567567",
         True, ["google.com", "something.com"], ["Python", "Negative 2 years of experience"]]
    ]


def test_filter_keyword(jobs):
    """Test jobs being filtered by user-given keyword correctly."""
    keyword = "Python"
    jobs = jobs_filtering.filter_keyword(jobs, keyword)
    assert len(jobs) == 1
    assert jobs[0][9][0] == keyword


def test_filter_city_location(jobs):
    """Test jobs being filtered by user-selected location correctly."""
    city = "New York"
    jobs = jobs_filtering.filter_city_location(jobs, city)
    assert len(jobs) == 2
    assert jobs[1][3] == city


def test_filter_remote(jobs):
    """Test jobs being filtered by remote selection correctly."""
    jobs = jobs_filtering.filter_remote(jobs, True)
    assert len(jobs) == 2
    assert jobs[0][7]


def test_filter_min_salary(jobs):
    """Test jobs being filtered by user-given minimum salary correctly."""
    user_min_salary = 110_000
    jobs = jobs_filtering.filter_min_salary(jobs, user_min_salary)
    assert len(jobs) == 2
    assert jobs[0][6] == "60 hourly"


def test_remove_parenthesis_in_location():
    """Test extra information in city string being removed correctly."""
    city = "Boston, MA (+2 others)"
    assert jobs_filtering.remove_parenthesis_in_location(city) == "Boston, MA"
