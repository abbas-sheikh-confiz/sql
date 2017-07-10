import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()

	# Create a new regions table
	c.execute("CREATE TABLE regions(city TEXT, region TEXT)")

	# Insert city enteris in table
	cities = [
				('New York City', 'Northeast'),
				('San Francisco', 'West'),
				('Chicago', 'Midwest'),
				('Houston', 'South'),
				('Phoenix', 'West'),
				('Boston', 'Northeast'),
				('Los Angeles', 'West'),
				('Houston', 'South'),
				('Philadelphia', 'Northeast'),
				('San Antonio', 'South'),
				('San Diego', 'West'),
				('Dallas', 'South'),
				('San Jose', 'West'),
				('Jacksonville', 'South'),
				('Indianapolis', 'Midwest'),
				('Austin', 'South'),
				('Detroit', 'Midwest')
			 ]
	c.executemany("INSERT INTO regions VALUES(?, ?)", cities)

	c.execute("SELECT * from regions ORDER BY region ASC")
	rows = c.fetchall()

	for row in rows:
		print(row[0], row[1])