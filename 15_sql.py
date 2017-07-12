# Homework for SQL functions
# Show car models and total number of orders
import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	# Read data from inventory table
	c.execute("SELECT Make, Model, Quantity FROM inventory")
	cars = c.fetchall()

	for car in cars:
		print("Car Maker: {} - Car Model: {}".format(car[0], car[1]))
		print("In House Quantity:", car[2])
		c.execute("SELECT count(order_date) FROM orders WHERE make = ? AND model = ?", (car[0], car[1]))
		orders_count = c.fetchone()[0]
		print("Total Orders:", orders_count)

