"""GUI using PySide6 to display all jobs to user, view job data of user-selected job, and allow user to filter jobs.
A map may also be displayed to show the locations of jobs."""

import re
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from mapwindow import MapWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, jobs):
        # Setup UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init jobs
        self.map_displayed = False
        self.JOBS = jobs
        self.filtered_jobs = self.JOBS  # Filtered jobs
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

        self.filter_remote()
        self.filter_min_salary()
        self.filter_keyword()
        self.filter_city_location()

        self.list_jobs()
        if self.map_displayed:
            self.update_map()
        self.deselect_job()

    def filter_keyword(self):
        """Search every job data fields to find whether they contain a string.

        Keyword arguments:
        None

        Returns:
        None
        """

        keyword = self.ui.keywordFilter_plainTextEdit.toPlainText()
        keyword_jobs = []

        for j in self.filtered_jobs:
            if self.keyword_in_job(keyword, j):
                keyword_jobs.append(j)

        self.filtered_jobs = keyword_jobs

    def keyword_in_job(self, keyword, job):
        """Find keyword in job's sublists.

        Keyword arguments:
        keyword -- string to be found in job data
        job -- list to be searched through for keyword

        Returns:
        Boolean for if keyword is found
        """

        # First 7 items are just strings. Last two (links, qualifications) are lists of strings.
        return (self.keyword_in_list(keyword, job[:7]) or
                self.keyword_in_list(keyword, job[-2]) or
                self.keyword_in_list(keyword, job[-1]))

    def keyword_in_list(self, keyword, l):
        """Searches list for keyword with null safety and case insensitivity.

        Keyword arguments:
        keyword -- string to be found in data
        l -- list of data to be searched for keyword

        Returns:
        Boolean for if keyword is found
        """

        if not l:
            return False
        for item in l:
            if keyword.lower() in item.lower():
                return True
        return False

    def insert_city_locations(self):
        """Gets cities of jobs and displays them for the user to select for location filtering.

        Keyword arguments:
        None

        Returns:
        None
        """

        cities = self.get_city_locations()
        self.ui.locationFilter_comboBox.addItem("")  # First item allows no city to be selected
        self.ui.locationFilter_comboBox.addItems(cities)

    def get_city_locations(self):
        """Gathers cities of jobs.

        Keyword arguments:
        None

        Returns:
        An alphabetically sorted set of cities
        """

        cities = set()
        for j in self.filtered_jobs:
            if j[3]:
                cities.add(self.get_city_str(j[3]))
        return sorted(cities)

    def get_city_str(self, city):
        """Formats a location like "Boston, MA" by removing text that isn't an address and removing the zipcode.

        Keyword arguments:
        city -- String of location

        Returns:
        city -- String of location formatted
        """

        city = self.remove_parenthesis_in_location(city)
        if re.search("[0-9-]+$", city):  # remove zipcode
            city = " ".join(city.split(" ")[:-1])
        return city

    def filter_city_location(self):
        """Filter jobs based on a city. User selects from available cities from jobs.

        Keyword arguments:
        None

        Returns:
        None
        """

        user_city = self.ui.locationFilter_comboBox.currentText()
        if not user_city:
            return
        city_jobs = []
        for j in self.filtered_jobs:
            if j[3] and user_city == self.get_city_str(j[3]):
                city_jobs.append(j)
        self.filtered_jobs = city_jobs

    def remove_parenthesis_in_location(self, city):
        """Cuts out text that isn't location like "Boston, MA (+2 others)"

        Keyword arguments:
        city -- Location to format

        Returns:
        city -- Formatted location
        """

        if "(" in city:  # remove "(+# others)" occurrences
            city = re.findall(".+\(", city)[0][:-1].rstrip()
        return city

    def filter_remote(self):
        """Either filter to only get remote jobs or ignore the information.

        Keyword arguments:
        None

        Returns:
        None
        """

        if self.ui.remoteFilter_checkBox.isChecked():
            self.filtered_jobs = [j for j in self.filtered_jobs if j[7]]
            # Way database works is it's either 1 or nothing.

    def filter_min_salary(self):
        """Filter jobs to only get what's at or above given yearly salary number.

        Keyword arguments:
        None

        Returns:
        None
        """

        user_min_salary = int(self.ui.salaryFilter_spinBox.value())
        min_salary_jobs = []

        for j in self.filtered_jobs:
            if user_min_salary <= self.get_yearly_salary(j[6]):
                min_salary_jobs.append(j)

        self.filtered_jobs = min_salary_jobs

    def get_yearly_salary(self, salary):
        """Filter jobs to only get what's at or above given yearly salary number.

        Keyword arguments:
        salary -- String of salary

        Returns:
        new_salary -- Float of yearly salary
        """

        if not salary:
            return 0

        new_salary = re.findall("^[0-9K.]+", salary)[0]

        if new_salary[-1] == "K":
            new_salary = float(new_salary[:-1]) * 1000
        else:
            new_salary = float(new_salary)

        rate = salary.split()[-1]
        if rate.startswith("hour"):  # could be "hourly"
            new_salary *= 40 * 52
        elif rate.startswith("week"):
            new_salary *= 52

        return new_salary

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

        jobs_to_display = self.format_jobs_for_map(self.filtered_jobs)
        self.jobs_map.add_locations(jobs_to_display)

    def format_jobs_for_map(self, jobs):
        """Prepare job data for map.

        Keyword arguments:
        jobs -- list of jobs

        Returns:
        jobs_to_display -- formatted jobs for map: (id, title, company, formatted location)
        """

        jobs_to_display = []
        for j in jobs:
            location = self.remove_parenthesis_in_location(j[3])
            curr_data = tuple(j[:3]) + (location,)
            jobs_to_display.append(curr_data)
        return jobs_to_display

    def map_window_closed(self):
        """Ensures no processing happens with map when it's not displayed.
        Needed because to use the map, it's created as a MainWindow member variable.

        Keyword arguments:
        None

        Returns:
        None
        """

        self.map_displayed = False
