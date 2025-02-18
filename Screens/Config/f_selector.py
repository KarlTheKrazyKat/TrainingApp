#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
#File Specific Imports
from Screens.Config.f_muscles import *

#Create Frame
f_selector = ttk.Frame(root,height=60,width=200,relief='sunken')
f_selector.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=(N, S, E, W))

#Configure Frame Grid
f_selector.columnconfigure(1,weight=1)
f_selector.rowconfigure(1,weight=1)

#Declare Stringvars

#Button Commands and Functions

#Navigation

#########################
#####Visual Elements#####
#########################

#Generate Muscle move over rows

with open("C:/Users/elija/OneDrive/Desktop/TrainingApp/muscles.cfg","r") as f:
    muscles = [line.strip() for line in f]
        
class Selector():
    def __init__(self,default,selected,list,addEntry = False):
        #currently add entry does nothing but it should in the future toggle the entry box when selected
        self.default = default
        self.selected = selected,
        self.list = list
        self.addEntry = addEntry

        for i in range(0,len(self.list),1):
            self.list[i] = Item(self.default,self.selected,i,text=self.list[i])

class Item(Selector):
    """Each item in the menu is created from the corresponding .json file. Each path should be given relative to xyz/WOM/
    """
    def __init__(self,default,selected,i,*args,**kwargs):
        #from parent
        self.default=default
        self.selected=selected
        #frame
        self.frame = ttk.Frame(self.default)
        self.frame.grid(column=1,row=i,sticky=(N, S, E, W))
        self.frame.columnconfigure(2,weight=1)
        self.frame.columnconfigure(1,weight=1)
        self.frame.rowconfigure(1,weight=1)
        #stringvar
        self.stringvar = StringVar()
        #self entry must be first so its drawn over
        self.entry = ttk.Entry(self.frame, textvariable=self.stringvar)
        self.entry.grid(column=2,row=1,sticky=(N, S, E, W))
        #self label
        self.label = ttk.Label(self.frame, *args, **kwargs)
        self.label.grid(column=1,row=1,sticky=(N, S, E, W))
        #self button
        self.button = ttk.Button(self.frame, text=">")
        self.button.grid(column=2,row=1,sticky=(N, S, E, W))
        
        self.root = root
        self.button.config(command = self.moveFrame)
        #self.button.pack()

    #will need to destroy self and draw to selected, then redraw selector with new list
    def moveFrame(self):
        if self.root == self.default:
            self.root == self.selected
            self.frame.columnconfigure(3,weight=1, minsize=0)
            self.button.grid(column=1,row=1,sticky=(N, S, E, W))
            self.button.configure(text="<")
            self.label.grid(column=2,row=1,sticky=(N, S, E, W))
            self.entry.grid(column=3,row=1,sticky=(N, S, E, W))
        else:
            self.root == self.default
            self.frame.columnconfigure(3,weight=0, minsize=0)
            self.entry.grid(column=1,row=1,sticky=(N, S, E, W))
            self.button.grid(column=2,row=1,sticky=(N, S, E, W))
            self.button.configure(text=">")
            self.label.grid(column=1,row=1,sticky=(N, S, E, W))
            
        self.rootUpdate()
    
    def rootUpdate(self):
        self.label.configure(root=self.root)
        self.button.configure(root=self.root)
            

muscleSelector = Selector(f_selector,f_muscles,muscles)