# Homework for SQL functions
# Count the car models
import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()
	car_models = {'Ford Mustang Count':
						"SELECT count(model) FROM orders WHERE model='Mustang' AND make='Ford'",
				  'Ford Fiesta Count':
						"SELECT count(model) FROM orders WHERE model='Fiesta' AND make='Ford'",
				   'Ford Galaxy Count':
						"SELECT count(model) FROM orders WHERE model='Galaxy' AND make='Ford'",
					'Honda Civic Count':
						"SELECT count(model) FROM orders WHERE model='Civic' AND make='Honda'",
					'Honda Accord Count':
						"SELECT count(model) FROM orders WHERE model='Accord' AND make='Honda'",
						}
	for key, value in car_models.items():
		c.execute(value)
		result = c.fetchone()
		print(key, result[0])
		print()
