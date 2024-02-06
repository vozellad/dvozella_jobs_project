"""Testing functions in main.py."""


import pytest
import main


def test_main():
    """Tests if method retrieves data using Serpapi and assures it gets at least 50 job listings."""

    jobs_results = []
    for page in range(5):
        jobs_results += main.get_jobs_results(page)
    assert len(jobs_results) >= 50
