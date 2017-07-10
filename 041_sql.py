# INSERT error handling using Try/Except
import sqlite3

with sqlite3.connect('new.db') as connection:
	cursor = connection.cursor()

	# Insert statement
	try:
		cursor.execute("INSERT INTO populations VALUES('New York', 'NY', 200000)")
		cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 8484848484)")

		# commit the changes
		conn.commit()
	except sqlite3.OperationalError as e:
		print(str(e))
		print('Oops! Something went wrong. Please try again')
