#!/usr/bin/env python

# Question 1
question1 = "1. What are the most popular three articles of all time?"

# Query 1 based on question 1
query1 = """
SELECT title, num
FROM (SELECT substr(path, 10), count(*) AS num
FROM log
WHERE path !='/' GROUP BY path)
AS hits, articles WHERE substr = slug
ORDER BY num DESC LIMIT 3;
"""

# Question 2
question2 = "2. Who are the most popular article authors of all time?"

# Query 2 based on question 2
query2 = """
SELECT authors_table.author, sum(views) AS views
FROM (SELECT authors.name AS author, articles.slug AS slug
FROM authors JOIN articles on authors.id = articles.author) AS authors_table
JOIN (SELECT path, count(*) AS views
FROM log  GROUP BY path ORDER BY views) AS newlog
ON replace(newlog.path,'/article/','') = authors_table.slug
GROUP BY authors_table.author ORDER BY views DESC;
"""

# Question 3
question3 = "3. On which days did more than 1% of requests lead to errors?"

# Query 3 based on question 3
query3 = """
SELECT *
FROM
(SELECT request_table.datedata,
    cast(round((errTable.error * 100.00)/request_table.request,2)
    AS numeric) AS err
FROM (SELECT count(*) AS request,date(log.time) AS datedata
FROM log GROUP by datedata) AS request_table
JOIN (SELECT count(*) AS error,date(log.time) AS datedata
FROM log WHERE log.status like '404%' GROUP by datedata) AS errTable
ON request_table.datedata=errTable.datedata) AS res WHERE err > 1;
"""

# list variable to map the questions
# that will be called by funtions defined in the main program
questions = [question1, question2, question3]

# list variable to map the SQL queries
# that will be called by funtions defined in the main program
queries = [query1, query2, query3]
