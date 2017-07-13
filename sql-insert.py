# ---- Example Application ---- #
# Script to insert random numbers
import sqlite3
import random

with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()

	# Create TABLE
	c.execute("CREATE TABLE IF NOT EXISTS Number(number INT)")

	# Insert 100 random integers between range(0-100)
	for i in range(0, 100):
		n = random.randint(0, 100)
		c.execute("INSERT INTO Number VALUES(?)", (n, ))
