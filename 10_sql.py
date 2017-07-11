import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()

	c.execute("""SELECT DISTINCT population.city, population.population, regions.region
					from population, regions 
						where population.city = regions.city
							ORDER BY population.city ASC""")
	rows = c.fetchall()

	for row in rows:
		print("City:", row[0])
		print("Population:", row[1])
		print("Region:", row[2])
		print("")
