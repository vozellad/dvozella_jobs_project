import sys
from unittest.mock import MagicMock
import pytest
from PySide6.QtWidgets import QApplication
import mapwindow


@pytest.fixture
def dummy_mapwindow():
    return mapwindow.MapWindow([])


@pytest.fixture(scope="session", autouse=True)
def setup_qapplication():
    app = QApplication(sys.argv)
    yield
    app.quit()


def test_geocode_location(dummy_mapwindow):
    dummy_mapwindow.geolocator.geocode = \
        MagicMock(return_value=MagicMock(latitude=42, longitude=-70))
    result = dummy_mapwindow.geocode_location("New York City, NY")
    assert result.latitude == 42
    assert result.longitude == -70
