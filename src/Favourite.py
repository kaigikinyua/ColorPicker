from tkinter import *
from ConvertColor import *
from DB import *
class Favourite:
    def __init__():
        self.favourite_frame=Tk()
        self.favourite_frame.title("Favourites")
        BuildFaveGui.buildFaveGui(self.favourite_frame)
        self.favourite_frame.mainloop()
    
class BuildFaveGui:
    @staticmethod
    def buildFaveGui(parent):
        #fetch colors->[iterate through the colors while building the gui]
        #append the generated colors gui to the self.favourite_frame
        pass

    @staticmethod
    def color_box(parent,color):
        colorBox=Frame(parent,width=100,height=100,bg=color)
        colorBox.pack()
    