Authors: Demetrios Vozella<br>

Project uses Python 3.10.<br><br>
Install Python modules 'serpapi' and 'google-search-results' for 'GoogleSearch'.<br>
Also install Python module 'sqlite3' and optionally install application 'DB Browser for SQLite' to view data.<br>

Create 'secrets.py' in the project directory, and initialize an 'api_key' variable with your api key.<br>
The secrets.py should be in the follwing format:&emsp;```api_key="your api key here"```<br>

Gets 5 pages google search jobs results, and stores the results in a text file.<br>
Also makes a database and stores it in 3 tables: 'jobs', 'related_links', and 'qualifications'.<br>
'jobs' table is the main table. 'related_links' stores multiple links for each job listing, and 'qualifications' stores multiple qualifications for each job listing.<br> 

Run the file, then view the text file it wrote to named 'jobs_results.txt'.<br>
Also use an application such as 'DB Browser for SQLite' to view the database.<br>

Nothing is missing up to sprint 2 (except for linter error which will be corrected soon).
