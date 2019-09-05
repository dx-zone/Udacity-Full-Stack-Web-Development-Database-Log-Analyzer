#!/usr/bin/env python

# Catch errors while importing library
try:
    # import DB API 2.0 compliant PostgreSQL driver as dbapi
    import psycopg2 as dbapi

except ImportError:
    print("""
        Can't find the psycopg2 module installed. Ensure the module get \
        installed.
        \n
        * For Python 2 execute: pip install psycopg2
        * For Python 3 execute: pip3 install psycopg2
        """)
    exit(1)

# Catch errors while importing variables from queries.py file
try:
    # to import questions and queries data from queries.py
    from queries import queries, questions

except ImportError:
    print("""Can't find the queries.py file.\
        Ensure the queries.py file is in the same directory as main.py file.
        """)
    exit(1)

# Creates a database connection object, exit the program if db connection fails
try:
    DB = dbapi.connect(database="news", user="vagrant")
    print("Successfully connected to database!\n")

except (Exception) as error:
    print("\n")
    print("Error while connecting to PostgreSQL database", error)
    print("""\nCheck the database management system (DBMS) to ensure the following:
        * DBSM is up and running
        * The DBSM port is accesible
        * Ensure the loganalyzer.py file matches the user name, password \
and the propper database name\n
        \tEx: DB = dbapi.connect(user = "sysadmin",
                                  password = "secret_password",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres_db_name")
        """)
    exit(1)


def execute_query(conn, query):
    """ This fuction is to execute database queries.
    Arguments:
        conn(dbapi.connect object): Database connection object
        query(string): Query to be executed by database
        ...
    """
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def print_response(questions, res, suff='views'):
    """ This fuction is to format and print queries output.
    Arguments:
        questions(string): questions
        res(list): query result object
        suff()string: suffix for output
        ...
    """
    print(questions)  # Print questions
    for i in range(len(res)):  # Format output
        print("\t{0}. {1} || {2} {3}".format(i+1, res[i][0], res[i][1], suff))
    print('\n')  # Print result


# disabled - to format last output individually - continues at line 90
# Calling the fuctions and looping through each
# queries and questions (lists variable) defined in queries.py
# i = 0
# while i < len(queries) and len(questions):
#     output = execute_query(DB, queries[i])
#     print_response(questions[i], output)
#     if i < len(queries) and len(questions):
#         i += 1

# Calling the functions and formatting output one at a time
ans1 = execute_query(DB, queries[0])
print_response(questions[0], ans1)
ans2 = execute_query(DB, queries[1])
print_response(questions[1], ans2)
ans3 = execute_query(DB, queries[2])

print(questions[2])
for i in range(len(ans3)):
    print("\t{0}. {1} || {2}% error".format(i+1, ans3[i][0], ans3[i][1]))
print('\n')

# Close Connction
DB.close()
