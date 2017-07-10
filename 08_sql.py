# Home Assignment: Update records
import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET Quantity = 123 WHERE Model = 'Accord'")
	c.execute("UPDATE inventory SET Quantity = 124 WHERE Model = 'Fiesta'")
	c.execute("UPDATE inventory SET Make = 'Honda' WHERE Model = 'Civic'")

	c.execute("SELECT * from inventory")
	rows = c.fetchall()

	for row in rows:
		print(row[0], row[1], row[2])
