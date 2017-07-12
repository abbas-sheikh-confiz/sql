# SQL Functions
import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	sql = {'Average': 'SELECT avg(population) FROM population',
		   'Maximum': 'SELECT max(population) FROM population',
		   'Minimum': 'SELECT min(population) FROM population',
		   'Count':   'SELECT count(population) FROM population',
		   'Sum': 	  'SELECT sum(population) FROM population'
	}

	for key, value in sql.items():
		c.execute(value)
		result = c.fetchone()
		print('Population {} is: {}'.format(key, result[0]))
