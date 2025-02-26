#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
from Screens.Config.f_selector import *
#File Specific Imports
from json import *

class Selector():
        """Each item in the menu is created from the corresponding .json file. Each path should be given relative to xyz/WOM/
        """
        def __init__(self,root,muscle,*args,**kwargs):
            self.frame = ttk.Frame(root)
            self.frame.columnconfigure(1,weight=1)
            self.frame.columnconfigure(2,weight=1)
            self.frame.rowconfigure(1,weight=1)
            self.label = ttk.Label(self.frame, text=muscle,justify="right")
            self.label.grid(column=1,row=1,sticky=(N, S, E, W))
            self.button = ttk.Button(self.frame, text = "Add To Plan", *args, **kwargs)
            self.button.grid(column=2,row=1,sticky=(N, S, E, W))

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