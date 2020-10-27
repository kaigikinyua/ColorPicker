from tkinter import *
from tkinter import messagebox
from ConvertColor import *
from DB import *
class CPicker:
	def __init__(self):
		self.root=Tk()
		self.root.title("ColorPicker")
	#create color and display panel
		self.createColor=LabelFrame(self.root,text="Create Color",width=100)
	#rectangle to view color created
		self.seeColor=Frame(self.createColor,width=100,height=100,bg="#FFFFFF")
		self.seeColor.pack()
	#enter values here to create color
		self.colorValues=Frame(self.createColor)
		rgbLabel=Label(self.colorValues,text="RGB values")
		rgbLabel.pack()
	#rgb spinboxes
		spinboxFrame=Frame(self.colorValues)
		self.rValue=Spinbox(spinboxFrame,from_=0,to=255,width=5)
		self.gValue=Spinbox(spinboxFrame,from_=0,to=255,width=5)
		self.bValue=Spinbox(spinboxFrame,from_=0,to=255,width=5)
		self.rValue.pack(side=LEFT);self.gValue.pack(side=LEFT);self.bValue.pack(side=LEFT)
		spinboxFrame.pack()
		hexLabel=Label(self.colorValues,text="Hex Codes")
		hexLabel.pack()
		self.hexValues=Entry(self.colorValues)
		self.hexValues.pack()
		self.colorValues.pack()
		self.changeColor=Button(self.colorValues,text="Generate",command=self.changeColor)
		self.changeColor.pack(fill=X)
		self.createColor.pack(side=LEFT,fill=Y)
	#actions panel
		self.actionsPanel=LabelFrame(self.root,text="Actions",width=100)
		self.seeFavourites=Button(self.actionsPanel,text="See Favourites")
		self.seeFavourites.pack(fill=X)
		self.addFavourite=Button(self.actionsPanel,text="Add to favourite")
		self.addFavourite.pack(fill=X)
		self.savecolor=Button(self.actionsPanel,text="Save Color",command=self.saveColor)
		self.savecolor.pack(fill=X)
		self.seeDiffColors=Button(self.actionsPanel,text="Explore Colors")
		self.seeDiffColors.pack(fill=X)
		self.actionsPanel.pack(side=RIGHT,fill=Y)
	#root window
		self.root.resizable(False,False)
		self.root.mainloop()

	def changeColor(self):
		ans=self.getHex()
		if(ans==False):
			hexV=self.hexValues.get()
			self.ErrorMsg(hexV+" is not a valid hex code")
		else:
			self.seeColor.configure(bg=ans)
	
	def saveColor(self):
		ans=self.getHex()
		hexV=self.hexValues.get()
		if(ans==False):
			self.ErrorMsg(hexV+" is not a valid hex code")
		else:
			db=DB()
			db.insert('SavedColors',hexV)

	def ErrorMsg(self,msg):
		messagebox.showerror('Error',msg)

	def getHex(self):
		hexV=self.hexValues.get()
		if(len(hexV)>0):
			c=Convert()
			ishex=c.confirmHex(hexV)
			if(ishex!=True):
				return False
			else:
				return hexV
		else:
			self.ErrorMsg("Cannot Process an empty field")

c=CPicker()
