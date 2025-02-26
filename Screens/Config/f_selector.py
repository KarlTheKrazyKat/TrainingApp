#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
#File Specific Imports
from Screens.Config.f_muscles import *
from json import *

#Create Frame
f_selector = ttk.Frame(root,height=60,width=200,relief='sunken')
f_selector.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=(N, S, E, W))

#Configure Frame Grid
f_selector.columnconfigure(1,weight=1)
f_selector.rowconfigure(2,weight=1)

#Declare Stringvars

#Button Commands and Functions

#Navigation

#########################
#####Visual Elements#####
#########################

#Generate Muscle move over rows

with open("../TrainingApp/muscles.cfg","r") as f:
    muscles = [line.strip() for line in f]

md = {}
for i in muscles:
    md[i]=False

with open("../TrainingApp/Screens/Config/Menus/selected.json","w") as f:
    dump(md, f, indent =2)


class Selector():
    """Each item in the menu is created from the corresponding .json file. Each path should be given relative to xyz/WOM/
    """
    def __init__(self,root,muscle,*args,**kwargs):
        self.label = ttk.Label(root, text=muscle,justify="right")
        self.button = ttk.Button(root, text = "Add To Plan", *args, **kwargs)
        self.root = root
        self.muscle = muscle
        self.button.config(command = self.select)

    def select(self):
        self.label.destroy()
        self.button.destroy()
        with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
            md = load(f)
        md[self.muscle]=True
        with open("../TrainingApp/Screens/Config/Menus/selected.json","w") as f:
            dump(md, f, indent =2)

c = 1
objects=["Empty"]#Says empty so appending starts at 1
for i in md:
    if md[i] == False:
        ob = Selector(f_selector,i)
        
        objects.append(ob)

        objects[c].label.grid(column=1,row=c,sticky=(N, S, E, W))
        objects[c].button.grid(column=2,row=c,sticky=(N, S, E, W))
        
        f_selector.rowconfigure(c,weight=1)
        c+=1