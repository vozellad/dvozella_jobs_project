import io
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable


class MapWindow(QWidget):
    def __init__(self, jobs):
        super().__init__()

        self._jobs = jobs
        self.geocode_cache = {}  # Simple in-memory cache

        self.setWindowTitle("Jobs Displayed on Map")
        self.window_width = 500
        self.window_height = 500
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.geolocator = Nominatim(user_agent="dvozella_jobs_project")

        coordinate = (39.828175, -98.5795)
        self.jobs_map = folium.Map(
            title="USA Center",
            zoom_start=4,
            location=coordinate
        )
        self.map_data_markers = MarkerCluster().add_to(self.jobs_map)

        self.build_map()

        self.in_memory_file = io.BytesIO()
        self.jobs_map.save(self.in_memory_file, close_file=False)

        self.web_view = QWebEngineView()
        self.web_view.setHtml(self.in_memory_file.getvalue().decode())
        self.layout.addWidget(self.web_view)

    def build_map(self):
        for j in self._jobs:
            title = j[0]
            company = j[1]
            location = j[2]

            if location in self.geocode_cache:
                job_loc_geocoded = self.geocode_cache[location]
            else:
                try:
                    job_loc_geocoded = self.geolocator.geocode(location)
                    if job_loc_geocoded:  # Cache successful geocode results
                        self.geocode_cache[location] = job_loc_geocoded
                except (GeocoderTimedOut, GeocoderUnavailable):
                    print(f"Geocoding failed for location: {location}")
                    continue

            if job_loc_geocoded:
                folium.Marker(
                    location=[job_loc_geocoded.latitude, job_loc_geocoded.longitude],
                    popup=f"{title}\n{company}"
                ).add_to(self.map_data_markers)
