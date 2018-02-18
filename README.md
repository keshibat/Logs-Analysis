# logs analysis project

###Project Overview

Build an internal reporting tool that will use information
from the database to discover what kind of articles the site's readers like.
My code create a reporting tool that prints out reports (in plain text) based on the data in the database.
This reporting tool is a Python program using the psycopg2 module to connect to the database.


#### 3 Questions
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [VirtualBox](https://www.virtualbox.org/)
    Currently (October 2017), the supported version of VirtualBox to install is version 5.1.
  * [Vagrant](https://www.vagrantup.com/)

### Files
* newsdata.sql
* newsdata.py
* vagrant file
* readme.md


#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the newsdata.zip from here. (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  4. Unzip and put this file[newsdata.sql] into the vagrant directory, which is shared with your virtual machine.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
     [Here](https://github.com/keshibat/Logs-Analysis)


#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

  ```
    $ vagrant up
  ```
  2. Then Log into this using command:

  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant




#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:

  '''
     psql -d news -f newsdata.sql

  '''
  The database includes three tables: you can see them using command: \d
  *article
  *authors
  *log

  Columns for each three tables:
  *article:columns(author/title/slug/lead/body/time/id)
  *authors:columns(name/bio/bio)
  *log:columns(path/ip/method/status/time/id/)


  2. Use `psql -d news` to connect to database.


###PSQL Command Used To create the view
#### article_view
'''
CREATE VIEW article_views AS
SELECT author, count(*) AS num_views
FROM articles, log
WHERE log.path = concat('/article/',articles.slug)
GROUP by articles.author
ORDER by num_views desc;

'''

#### the total requests for that day
'''
CREATE VIEW total_request AS
SELECT count(*) AS count,
       date(time) AS date
FROM log
GROUP BY date
ORDER BY count DESC;
'''


#### the total Error requests for that day
'''
CREATE VIEW total_error AS
SELECT count(*) AS count,
       date(time) AS date
FROM log
Where status!='200 OK'
GROUP BY date
ORDER BY count DESC;
'''

#### the percent error for that day
'''
CREATE VIEW percent_error AS
SELECT total_request.date,
       (total_error.count::float / total_request.count::float)* 100 AS perc
from total_request,
     total_error
where total_error.date=total_request.date;
'''


#### The Python Reporting Tool
  * After the Views have been created, inside the virtual machine run `news.py` with -
  ```python
  python news.py
  ```
  * The python file `news.py` executes 3 functions, printing out the answers onto the terminal.