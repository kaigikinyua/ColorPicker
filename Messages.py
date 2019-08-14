from tkinter import messagebox

class Messages:
	def __init__(self,msgtype,msg):
		if(msgtype=='error'):
			messagebox.showerror('Error',msg)