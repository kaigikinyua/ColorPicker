import sqlite3

class DB:
	def __init__(self):
		try:
			self.db=sqlite3.connect('./Colors.db')
			print("Connected to database")
		except:
			print("Error Connecting to database")

d=DB()