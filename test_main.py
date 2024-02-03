import pytest
import main


def test_main():
    jobs_results = []
    for page in range(5):
        jobs_results += main.get_jobs_results(page)
    assert len(jobs_results) >= 50
