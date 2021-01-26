import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        row = [("Bob", 21, "1990-02-06 23:04:56"),
               ("Bob", 56, "1955-05-09 23:04:56"),
               ("Bob", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was
    # successful
    connection.close()