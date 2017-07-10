# SELECT statement
import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()

	# read rows from the table
	# for row in cursor.execute("SELECT firstname, lastname FROM employees"):
	# 	print (row)

	# Read from DB table
	c.execute("SELECT firstname, lastname FROM employees")
	rows = c.fetchall()

	# print records on screen
	for row in rows:
		print(row[0], row[1])
