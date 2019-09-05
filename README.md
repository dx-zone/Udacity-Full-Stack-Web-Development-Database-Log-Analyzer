## Database Log Analysis (Log Analyzer)

### Description

This program can be use as a reporting tool in order to answers questions by quering a database (based on pre-defined SQL queries beforehand). The print out results can serve as a base for data analysis.

This program is design to run by a **Python interpreter** and it consists of two (2) files. The **loganalyzer.py** and the  **queries.py**.

The **loganalyzer.py** is the main program.  This program will establish the connection to the database and execute a set of queries then print out in well-formatted text output (the results) to answer to the following question based on the data in the given database:

* **What are the most popular three articles of all time?** 

* **Who are the most popular article authors of all time?**

* **On which days did more than 1% of requests lead to errors?** 

The secondary file of the program is **queries.py** which contains the text or title of the question given before hand which are associated to SQL commands (or SQL queries) in this same file for the **loganalyzer.py** program to gather the data out of the database and to print out the results.

Splitting the program in two file will provide the flexibility to add, remove or modify any question/query desired directly in the **queries.py** file without altering the main functions of  the **loganalyzer.py** program.  In this way the **queries.py** can be adapted to define SQL commands for any data we might need the **loganalyzer.py** program to extract from the database.



### Requirements

* Python (2 or 3)
* Psycopg2, a DB API 2.0 compliant PostgreSQL driver, that enables the program to establish a database connection to gather data out if it.
* PostgreSQL object-relational database system with the appropriate database loaded.
* Vagrant "an open-source software product for building and maintaining portable virtual software development environments"
* Virtual Machine Hosted Hypervisor
  * [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for Linux, Windows or Mac OS (free)
  * [VMware Workstation](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html) for Windows with Vagrant VMware-Desktop-Plugin (paid)
  * [VMware Fusion](https://my.vmware.com/en/web/vmware/info/slug/desktop_end_user_computing/vmware_fusion/11_0) for Mac OS with Vagrant VMware-Desktop-Plugin (paid)



### Installation

* Python (refer to [Python.org](Python.org) for installation instructions)
* Vagrant (refer to [Vagrantup.com](https://www.vagrantup.com/docs/installation/) for installation instructions)
* git clone https://github.com/dx-zone/Udacity---Full-Stack-Web-Developer---Database-Log-Analysis-Log-Analyzer-
* cd Udacity---Full-Stack-Web-Developer---Database-Log-Analysis-Log-Analyzer-
* Launch and connect to the Vagrant VM:
   * `vagrant up`
   * `vagrant ssh`
   * `$ cd /vagrant`
* Install psycopg2 for Python2: 
  ```pip install psycopg2```
* Install psycopg2 for Python3: 
   `pip3 install psycopg2`
* Launch PostgreSQL interactive terminal, create the a database then import the newsdata.sql data (replace data inside < > fields to match your database, user and password information):
   * `psql`
   * `create database news;`
   * `create user <database username> with encrypted password '<password>';`
   * `grant all privileges on database <database name> to <database username>;`
   * `psql -d news -f newsdata.sql`
* Update the **loganalyzer.py** file as necessary with the database name, user and password information. Ex:
   * `DB = dbapi.connect(user = "sysadmin", password = "secret_password", host = "127.0.0.1", port = "5432", database = "postgres_db_name")`



### To Run The Program

To run the program execute:
`python loganalyzer.py`

The **loganalyzer.py** program will look for the questions defined in the **queries.py** script as a list variable (named as questions) as well as the SQL commands defined as list (named as queries).  Once the **loganalyzer.py** import the variables that defines the questions and the SQL commands it will connect to the PostgreSQL database (database named as "news") to execute the SQL queries and print out the title of the questions as well as the results gathered from the queries.



###Author

* Daniel Cruz - [dx-zone](https://github.com/dx-zone)

