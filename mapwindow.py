import io

import folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QVBoxLayout, QWidget


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jobs Displayed on Map")
        self.window_width = 500
        self.window_height = 500
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (39.828175, -98.5795)
        m = folium.Map(
            title="USA Center",
            zoom_start=4,
            location=coordinate
        )

        data = io.BytesIO()
        m.save(data, close_file=False)

        web_view = QWebEngineView()
        web_view.setHtml(data.getvalue().decode())
        layout.addWidget(web_view)
