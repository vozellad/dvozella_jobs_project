import pytest
import mainwindow


@pytest.fixture
def main_window():
    # Mock jobs data for testing
    jobs = [
        ["1", "Software Engineer", "ABC Inc.", "New York", "Job description...", "2024-03-01", "100K", True, [], []],
        ["2", "Data Scientist", "XYZ Corp.", "San Francisco", "Job description...", "2024-03-02", "120K", False, [], []],
        ["3", "Product Manager", "123 Co.", "Los Angeles", "Job description...", "2024-03-03", "150K", True, [], []]
    ]
    return mainwindow.MainWindow(jobs)


def test_filter_keyword():
    pass
