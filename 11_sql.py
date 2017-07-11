# Homework for joins
import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()
	
	# create a new table
	c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

	# insert records in the table
	orders = [('Ford', 'Mustang', '2017-06-15'),
			  ('Ford', 'Mustang', '2017-06-16'),
			  ('Ford', 'Mustang', '2017-06-17'),

			  ('Ford', 'Fiesta', '2017-06-18'),
			  ('Ford', 'Fiesta', '2017-06-19'),
			  ('Ford', 'Fiesta', '2017-06-20'),

			  ('Ford', 'Galaxy', '2017-06-21'),
			  ('Ford', 'Galaxy', '2017-06-22'),
			  ('Ford', 'Galaxy', '2017-06-23'),

			  ('Honda', 'Accord', '2017-06-24'),
			  ('Honda', 'Accord', '2017-06-25'),
			  ('Honda', 'Accord', '2017-06-26'),

			  ('Honda', 'Civic', '2017-06-27'),
			  ('Honda', 'Civic', '2017-06-28'),
			  ('Honda', 'Civic', '2017-06-29'),]
	c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
