"""Testing functions in mainwindow.py"""

import pytest
from PySide6.QtWidgets import QApplication

import mainwindow


@pytest.fixture
def dummy_mainwindow():
    jobs = [
        ["1", "Software Engineer", "ABC Inc.", "New York", "Job description...", "2024-03-01", "100K - 120K",
         True, [], []],
        ["2", "Data Scientist", "XYZ Corp.", "San Francisco", "Job description...", "2024-03-02", "60 hourly",
         False, [], []],
        ["3", "Product Manager", "123 Co.", "New York", "Job description...", "2024-03-03", "150000 - 567567",
         True, ["google.com", "something.com"], ["Python", "Negative 2 years of experience"]]
    ]
    return mainwindow.MainWindow(jobs)


@pytest.fixture(scope="session", autouse=True)
def setup_qapplication():
    app = QApplication([])
    yield
    app.quit()


def test_filter_keyword(dummy_mainwindow):
    """Test jobs being filtered by user-given keyword correctly."""
    dummy_mainwindow.ui.keywordFilter_plainTextEdit.setPlainText("python")
    dummy_mainwindow.filter_keyword()
    assert len(dummy_mainwindow.filtered_jobs) == 1
    assert dummy_mainwindow.filtered_jobs[0][9][0] == "Python"


def test_filter_city_location(dummy_mainwindow):
    """Test jobs being filtered by user-selected location correctly."""
    dummy_mainwindow.ui.locationFilter_comboBox.setCurrentText("New York")
    dummy_mainwindow.filter_city_location()
    assert len(dummy_mainwindow.filtered_jobs) == 2
    assert dummy_mainwindow.filtered_jobs[1][3] == "New York"


def test_filter_remote(dummy_mainwindow):
    """Test jobs being filtered by remote selection correctly."""
    dummy_mainwindow.ui.remoteFilter_checkBox.setChecked(True)
    dummy_mainwindow.filter_remote()
    assert len(dummy_mainwindow.filtered_jobs) == 2
    assert dummy_mainwindow.filtered_jobs[0][7]


def test_filter_min_salary(dummy_mainwindow):
    """Test jobs being filtered by user-given minimum salary correctly."""
    dummy_mainwindow.ui.salaryFilter_spinBox.setValue(110_000)
    dummy_mainwindow.filter_min_salary()
    assert len(dummy_mainwindow.filtered_jobs) == 2
    assert dummy_mainwindow.filtered_jobs[0][6] == "60 hourly"
