import sqlite3
from Messages import *

class ColorsDB:
	def fetchFaveColors(self):
		d=DB()
		colors=d.select("favourite","*","hexvalue")
		return colors

	def fetchTemplate(self,templatename):
		d=DB()
		colors=d.select("template",templatename,"templatename")
		return colors

class DB:
	def __init__(self):
		try:
			self.db=sqlite3.connect('./Colors.db')
		except:
			E=Messages('error','Error during Storage')
			
	def select(self,tablename,param,column):
		sql=""
		if(len(tablename)>0 and len(param)>0 and len(column)>0):
			if param=='*':
				sql="SELECT * from "+tablename
			else:
				sql="SELECT * from "+tablename+" WHERE "+column+" = '"+param+"'"
			c=self.db.cursor()
			#print(sql)
			c.execute(sql)
			data=c.fetchall()
			#print(data)
			return data
		else:
			E=Messages('Empty Field','Please make sure all the parameters are filled')
			return False

	def insert(self,tablename,param):
		sql=""
		if(len(tablename)>0 and len(param)>0):
			sql="INSERT INTO '%s' VALUES('%s')"%(tablename,param)
			c=self.db.cursor()
			c.execute(sql)
			self.db.commit()
		else:
			E=Messages('Empty Field','Please make sure all the parameters are filled')

c=ColorsDB()
print(c.fetchFaveColors())
print(c.fetchTemplate("test"))