import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()

	# Update records
	c.execute("UPDATE population SET population = 9292992 WHERE city = 'New York City'")

	# delete records
	c.execute("DELETE FROM population WHERE city = 'Boston'")

	print('\nNew Data: \n')

	c.execute('SELECT * from population')

	rows = c.fetchall()

	for row in rows:
		print(row)
