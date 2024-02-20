"""Testing functions in jobs_results.py."""


import pytest
import jobs_results


def test_main():
    """Tests if method retrieves data using Serpapi and assures it gets 50 job listings."""

    jobs = jobs_results.get_jobs(5)
    assert len(jobs) == 50
