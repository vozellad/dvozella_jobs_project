"""GUI using PySide6 to display all jobs to user, view job data of user-selected job, and allow user to filter jobs.
A map may also be displayed to show the locations of jobs."""

import re
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from mapwindow import MapWindow
from ui_mainwindow import Ui_MainWindow
import jobs_filtering


class MainWindow(QWidget):
    def __init__(self, jobs):
        # Setup UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init jobs
        self.map_displayed = False
        self.JOBS = jobs
        self.filtered_jobs = self.JOBS
        self.list_jobs()
        self.ui.jobs_listWidget.selectionModel().currentChanged.connect(self.job_selected)

        # Init deselect button
        self.ui.deselect_pushButton.clicked.connect(self.deselect_job)

        # Init map
        self.jobs_map = MapWindow([])
        self.jobs_map.windowClosed.connect(self.map_window_closed)
        self.ui.map_pushButton.clicked.connect(self.display_map)

        # Init filters
        self.ui.applyFilters_pushButton.clicked.connect(self.filter_jobs)
        self.insert_city_locations()
        self.ui.filter_gridLayout.setAlignment(self.ui.applyFilters_pushButton, Qt.AlignmentFlag.AlignRight)

    def list_jobs(self):
        """Re-fills list widget (that hosts jobs for the user to select) with the currently selected jobs
        or all jobs if it's called as the window is created.

        Keyword arguments:
        None

        Returns:
        None
        """

        # Don't append to previous existing list
        self.ui.jobs_listWidget.clear()

        for j in self.filtered_jobs:
            job_str = f"{j[1]}\n{j[2]}"  # Get title and company as text
            self.ui.jobs_listWidget.addItem(job_str)

        # Display amount of jobs
        self.ui.resultsAmt_label.setText(str(len(self.filtered_jobs)))

    def job_selected(self, current, previous):
        """Clicked event for list item being selected in list to display jobs.
        When user selects new job, data from that job is displayed in more detail.

        Keyword arguments:
        current -- Current list index of job selected
        previous -- Previous list index of job selected
                    (right as the clicked event happened, and it hasn't fully transitioned to the new selection yet)

        Returns:
        None
        """

        # Boxes will be empty on window startup
        if previous.row() == -1:
            self.set_placeholders()

        # If row is set programmatically to select nothing
        if current.row() == -1:
            return

        # Fill boxes with data of selected job
        self.set_job_fields(self.filtered_jobs[current.row()])

        # Remove multiple odd behaviors related to user clicking on list widget
        self.ui.jobs_listWidget.setFocus(Qt.FocusReason.MouseFocusReason)
        self.ui.jobs_listWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def deselect_job(self):
        """Removes the focus on a job in the job-list, and removes the selected job data being displayed.

        Keyword arguments:
        None

        Returns:
        None
        """

        # Remove the focus of the selected job
        self.ui.jobs_listWidget.clearSelection()
        self.clear_job_fields()
        self.clear_placeholders()

        # Remove multiple odd behaviors related to user clicking on list widget
        self.ui.jobs_listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def set_placeholders(self):
        """Change the placeholder text of the boxes holding selected job data to the default text for that field.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.ui.title_plainTextEdit.setPlaceholderText("Not available")
        self.ui.company_plainTextEdit.setPlaceholderText("Not available")
        self.ui.location_plainTextEdit.setPlaceholderText("Not available")
        self.ui.description_plainTextEdit.setPlaceholderText("Not available")
        self.ui.postedAt_plainTextEdit.setPlaceholderText("Not available")
        self.ui.salary_plainTextEdit.setPlaceholderText("Not available")
        self.ui.remote_plainTextEdit.setPlaceholderText("No")
        self.ui.links_plainTextEdit.setPlaceholderText("Not available")
        self.ui.qualifications_plainTextEdit.setPlaceholderText("Not available")

    def clear_placeholders(self):
        """Change the placeholder text of the boxes holding selected job data to be empty.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.ui.title_plainTextEdit.setPlaceholderText("")
        self.ui.company_plainTextEdit.setPlaceholderText("")
        self.ui.location_plainTextEdit.setPlaceholderText("")
        self.ui.description_plainTextEdit.setPlaceholderText("")
        self.ui.postedAt_plainTextEdit.setPlaceholderText("")
        self.ui.salary_plainTextEdit.setPlaceholderText("")
        self.ui.remote_plainTextEdit.setPlaceholderText("")
        self.ui.links_plainTextEdit.setPlaceholderText("")
        self.ui.qualifications_plainTextEdit.setPlaceholderText("")

    def set_job_fields(self, job):
        """Change the text of the boxes holding selected job data to include the job data relevant for each field.

        Keyword arguments:
        None

        Returns:
        None
        """

        # Displays data if available
        self.ui.title_plainTextEdit.setPlainText(job[1] if job[1] else "")
        self.ui.company_plainTextEdit.setPlainText(job[2] if job[2] else "")
        self.ui.location_plainTextEdit.setPlainText(job[3] if job[3] else "")
        self.ui.description_plainTextEdit.setPlainText(job[4] if job[4] else "")
        self.ui.postedAt_plainTextEdit.setPlainText(job[5] if job[5] else "")
        self.ui.salary_plainTextEdit.setPlainText(job[6] if job[6] != "0" else "")
        self.ui.remote_plainTextEdit.setPlainText("Yes" if job[7] else "")
        self.ui.links_plainTextEdit.setPlainText('\n'.join(job[-2]) if job[-2] else "")
        self.ui.qualifications_plainTextEdit.setPlainText('\n'.join(job[-1]) if job[-1] else "")

    def clear_job_fields(self):
        """Change the text of the boxes holding selected job data to be empty so no job data is displayed.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.ui.title_plainTextEdit.setPlainText("")
        self.ui.company_plainTextEdit.setPlainText("")
        self.ui.location_plainTextEdit.setPlainText("")
        self.ui.description_plainTextEdit.setPlainText("")
        self.ui.postedAt_plainTextEdit.setPlainText("")
        self.ui.salary_plainTextEdit.setPlainText("")
        self.ui.remote_plainTextEdit.setPlainText("")
        self.ui.links_plainTextEdit.setPlainText("")
        self.ui.qualifications_plainTextEdit.setPlainText("")

    def filter_jobs(self):
        """Clicked event for when user applies filters.
        Filter jobs in list and what's displayed on list and map.
        Filter jobs by:
            Remote (checkbox): Either filter to only get remote jobs or ignore the information.
            Minimum salary (spinbox): Filter jobs to only get what's at or above given yearly salary number.
            Keyword (textedit): Search all job data to find whether it contains a string.
            Location (combobox): Filter jobs based on a city. User selects from available cities from jobs.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.filtered_jobs = self.JOBS

        remote_checked = self.ui.remoteFilter_checkBox.isChecked()
        self.filtered_jobs = jobs_filtering.filter_remote(self.filtered_jobs, remote_checked)

        user_min_salary = int(self.ui.salaryFilter_spinBox.value())
        self.filtered_jobs = jobs_filtering.filter_min_salary(self.filtered_jobs, user_min_salary)

        keyword = self.ui.keywordFilter_plainTextEdit.toPlainText()
        self.filtered_jobs = jobs_filtering.filter_keyword(self.filtered_jobs, keyword)

        user_city = self.ui.locationFilter_comboBox.currentText()
        self.filtered_jobs = jobs_filtering.filter_city_location(self.filtered_jobs, user_city)

        self.list_jobs()
        if self.map_displayed:
            self.update_map()
        self.deselect_job()

    def insert_city_locations(self):
        """Gets cities of jobs and displays them for the user to select for location filtering.

        Keyword arguments:
        None

        Returns:
        None
        """

        cities = jobs_filtering.get_city_locations(self.filtered_jobs)
        self.ui.locationFilter_comboBox.addItem("")  # First item allows no city to be selected
        self.ui.locationFilter_comboBox.addItems(cities)

    def display_map(self):
        """Creates map window to display job locations. Jobs that are displayed in list gets displayed on map.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.map_displayed = True
        self.add_jobs_to_map()
        self.jobs_map.show()

    def update_map(self):
        """Remove jobs displayed on map and re-enter currently filtered jobs on map.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.add_jobs_to_map()

    def add_jobs_to_map(self):
        """Marks currently filtered jobs' locations on map.

        Keyword arguments:
        None

        Returns:
        None
        """

        jobs_to_display = jobs_filtering.format_jobs_for_map(self.filtered_jobs)
        self.jobs_map.add_locations(jobs_to_display)

    def map_window_closed(self):
        """Ensures no processing happens with map when it's not displayed.
        Needed because to use the map, it's created as a MainWindow member variable.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.map_displayed = False
