# Home Assignment: Add new records

import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	records = [('Ford', 'Mustang', 341),
			   ('Ford', 'Fiesta', 200),
			   ('Ford', 'Galaxy', 443),
			   ('Honda', 'Accord', 344),
			   ('Honda', 'Civic', 343)]
	c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", records)
