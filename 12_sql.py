# Homework to insert 
import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	# c.execute("""SELECT inventory.Make, inventory.Model, inventory.Quantity, orders.order_date
	# 			 FROM inventory, orders WHERE inventory.Model = orders.model 
	# 			 ORDER BY orders.order_date ASC""")
	c.execute("""SELECT inventory.Make, inventory.Model, inventory.Quantity, orders.order_date
				 FROM inventory INNER JOIN orders ON inventory.Model = orders.model 
				 ORDER BY orders.order_date ASC""")
	rows = c.fetchall()

	for row in rows:
		print("Car Make: {} - Model: {}".format(row[0], row[1]))
		print("Quantity:", row[2])
		print("Order Date:", row[3])
		print()
