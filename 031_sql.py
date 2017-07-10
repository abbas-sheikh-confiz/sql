# INSERT using exectemany statement
# import sqlite3 library
import sqlite3

with sqlite3.connect('new.db') as connection:
	cursor = connection.cursor()
	# insert multiple records using tuple
	cities = [('Lahore', 'PN', 1500000),
				('Karachi', 'SD', 2000000),
				('Peshawer', 'KP', 1000000 )]
	cursor.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)