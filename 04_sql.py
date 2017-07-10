# CSV reader
import csv
import sqlite3

with sqlite3.connect('new.db') as connection:
	cursor = connection.cursor()

	# import a csv file and assign it to a variable
	employees = csv.reader(open('employees.csv', 'rU'))

	# create a new table for employees
	cursor.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	# insert employee data into table
	cursor.executemany("INSERT INTO employees VALUES(?, ?)", employees)
	

	