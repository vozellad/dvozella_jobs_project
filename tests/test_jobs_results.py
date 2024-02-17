"""Testing functions in main.py."""


import pytest
import jobs_results


def test_main():
    """Tests if method retrieves data using Serpapi and assures it gets at least 50 job listings."""

    jobs = []
    for page in range(5):
        jobs += jobs_results.get_jobs(page)
    assert len(jobs) >= 50
