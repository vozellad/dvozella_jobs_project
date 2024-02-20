Authors: Demetrios Vozella<br>

Project uses Python 3.10.<br><br>
Install application 'DB Browser for SQLite' to view data.<br>

Create 'my_secrets.py' in the project directory, and initialize an 'api_key' variable with your api key.<br>
The 'my_secrets.py' should be in the follwing format:&emsp;```api_key="your api key here"```<br>

Gets 5 pages of Google search jobs results via Serpapi and stores the results in a text file.<br>
Gets jobs from an Excel file.<br>

Makes a database and stores it in 3 tables: 'jobs', 'related_links', and 'qualifications'.<br>
'jobs' table is the main table. 'related_links' stores multiple links for each job listing, and 'qualifications' 
stores multiple qualifications for each job listing.<br>

Order of data: (job_id, title, company_name, location, description, posted_at, salary, remote, links, qualifications)

Run the file, then view the text file it wrote to named 'jobs_results.txt'.<br>
Use an application such as 'DB Browser for SQLite' to view the database.<br>

Nothing is missing for Sprint 3

