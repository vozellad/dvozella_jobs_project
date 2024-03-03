"""Window displaying a map used to display locations of jobs."""

import io

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable


class MapWindow(QWidget):
    windowClosed = Signal()

    def __init__(self, jobs):
        super().__init__()

        self.map_data_markers = None
        self.jobs_map = None
        self.geolocator = None
        self.web_view = QWebEngineView()
        self.in_memory_file = None
        self.geocode_cache = {}

        self.setWindowTitle("Jobs Displayed on Map")
        self.window_width = 500
        self.window_height = 500
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.init_map()
        self.add_locations(jobs)

        self.layout.addWidget(self.web_view)

    def init_map(self):
        """Creates empty map. Centers view on the USA. Prepares markers to be clustered.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.geolocator = Nominatim(user_agent="dvozella_jobs_project")
        coordinate = (39.828175, -98.5795)
        self.jobs_map = folium.Map(
            title="USA Center",
            zoom_start=4,
            location=coordinate
        )
        self.map_data_markers = MarkerCluster().add_to(self.jobs_map)

    def refresh_map(self):
        """Displays new markers added.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.in_memory_file = io.BytesIO()
        self.jobs_map.save(self.in_memory_file, close_file=False)
        self.web_view.setHtml(self.in_memory_file.getvalue().decode())

    def add_locations(self, jobs):
        """Adds new markers of job locations on map.

        Keyword arguments:
        jobs -- job data (id, title, company, location)

        Returns:
        None
        """

        # Remove all markers on map (since markers can't be removed)
        self.clear()

        for job_id, title, company, location in jobs:
            # Get coordinates of location
            job_loc_geocoded = self.geocode_location(location)
            if not job_loc_geocoded:
                continue

            # Add location to map
            marker = folium.Marker(
                location=[job_loc_geocoded.latitude, job_loc_geocoded.longitude],
                popup=f"{title}\n\n{company}"
            )
            marker.add_to(self.map_data_markers)
            marker.job_id = job_id

        self.refresh_map()

    def geocode_location(self, location):
        """Gets coordinates of location.

        Keyword arguments:
        location -- Location string

        Returns:
        Location coordinates
        """

        # Don't query for coordinates if already done so before
        if location in self.geocode_cache:
            return self.geocode_cache[location]

        try:
            # Get coordinates of location
            job_loc_geocoded = self.geolocator.geocode(location)
            if job_loc_geocoded:
                self.geocode_cache[location] = job_loc_geocoded
                return job_loc_geocoded
        except (GeocoderTimedOut, GeocoderUnavailable):
            print(f"Geocoding failed for location: {location}")

        return None

    def closeEvent(self, event):
        """Event of window closing.

        Keyword arguments:
        event -- Window closing

        Returns:
        None
        """

        self.windowClosed.emit()
        event.accept()

    def clear(self):
        """Re-build map so it has no markers.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.init_map()
        self.refresh_map()
