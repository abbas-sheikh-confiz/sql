# Create cars database
import sqlite3

# create cars database
conn = sqlite3.connect('cars.db')

# create cursor
c = conn.cursor()

# create inventory table
c.execute("""CREATE TABLE inventory
			(Make TEXT, Model TEXT, Quantity INT)
			""")

# close the connection
c.close()
