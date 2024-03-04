Authors: Demetrios Vozella<br>

Project uses Python 3.10.<br>

GUI was made in Qt Creator using Qt6 with PySide6.<br>
After each ui modification, a terminal line converts it from a .ui file to a .py file so the project can reference and 
use it. Both files are included in this repository.<br>

The following terminal line is used after editing the GUI form. This can also be done manually. 
```pyside6-uic /Path/To/QtCreator/Project/form.ui -o /Path/To/This/Project/ui_mainwindow.py```

If you would like to view the database, install the application 'DB Browser for SQLite'.<br>

Create 'my_secrets.py' in the project directory, and initialize an 'api_key' variable with your api key.<br>
The 'my_secrets.py' should be in the following format:&emsp;```api_key="your api key here"```<br>

Gets 5 pages of Google search jobs results via Serpapi and stores the results in a text file.<br>
Gets jobs from an Excel file.<br>

Makes a database and stores it in 3 tables: 'jobs', 'related_links', and 'qualifications'.<br>
'jobs' table is the main table. 'related_links' stores multiple links for each job listing, and 'qualifications' 
stores multiple qualifications for each job listing.<br>

Order of data: (job_id, title, company_name, location, description, posted_at, salary, remote, links, qualifications)<br>
Both data sources go into the same database and set of tables.<br>

Program provides a graphical user interface for viewing jobs data.<br>
User is able to filter by keyword, location, minimum salary, and if the job's remote.<br>
Locations of jobs can be displayed on a map.<br>

Run the main.py file in the directory.<br>
You can view a text file it wrote to named 'jobs_results.txt'.<br>
If you need to view the database, use an application such as 'DB Browser for SQLite'.<br>
The GUI will also start when executing the program.<br>

Click the Map button to view the locations of the jobs.<br>
The more jobs currently listed, the longer it will take for the map to build.<br>

What is missing for Sprint 4 is making the GUI tests run headless so GitHub actions can run them. 
