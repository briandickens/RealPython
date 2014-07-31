# import from CSV

# import the csv library

import sqlite3

import csv

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable

    employees = csv.reader(open('employees.csv', 'rU'))

    # create a new table called employees
    c.execute("CREATE TABLE employees(firstname, lastname)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)

