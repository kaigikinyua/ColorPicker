from tkinter import *

class CPicker:
	def __init__(self):
		self.root=Tk()
		self.root.title("ColorPicker")
		#create color and display panel
		self.createColor=LabelFrame(self.root,text="Create Color",width=100)
		self.seeColor=Frame(self.createColor,width=100,height=100,bg="#FFFFFF")
		self.seeColor.pack()

		self.colorValues=Frame(self.createColor)
		rgbLabel=Label(self.colorValues,text="RGB values")
		rgbLabel.pack()
		self.rgbValues=Entry(self.colorValues)
		self.rgbValues.pack()
		self.createColor.pack(side=LEFT,fill=Y)
		self.colorValues.pack()
		#actions panel
		self.actionsPanel=LabelFrame(self.root,text="Actions",width=100)
		self.addFavourite=Button(self.actionsPanel,text="Add to favourite")
		self.addFavourite.pack()
		self.savecolor=Button(self.actionsPanel,text="Save Color")
		self.savecolor.pack()
		self.actionsPanel.pack(side=RIGHT,fill=Y)
		self.root.mainloop()

c=CPicker()
