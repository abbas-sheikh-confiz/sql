# ---- Example Application ---- #
# Script to aggregate numbers
import sqlite3
import os

def average(cursor):
	cursor.execute("SELECT avg(number) FROM Number")
	result = cursor.fetchone()[0]
	print('Number Average is:', result)
def max(cursor):
	cursor.execute("SELECT max(number) FROM Number")
	result = cursor.fetchone()[0]
	print('Maximum Number is:', result)
def min(cursor):
	cursor.execute("SELECT min(number) FROM Number")
	result = cursor.fetchone()[0]
	print('Minimum Number is:', result)
def sum(cursor):
	cursor.execute("SELECT sum(number) FROM Number")
	result = cursor.fetchone()[0]
	print('Sum of all numbers:', result)


if __name__ == "__main__":
	with sqlite3.connect('newnum.db') as connection:
		c = connection.cursor()
		while(1):
			print("Press 1 for Average")
			print("Press 2 for Max")
			print("Press 3 for Min")
			print("Press 4 for Sum")
			print("Press 5 to Quit")
			user_input = input("Your choice?: ")
			user_input = int(user_input)
			if user_input == 1:
				average(c)
			elif user_input == 2:
				max(c)
			elif user_input == 3:
				min(c)
			elif user_input == 4:
				sum(c)
			else:
				break
			# os.system('clear')
