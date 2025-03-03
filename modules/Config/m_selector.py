#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
#File Specific Imports
from Screens.Config.f_selector import *
from Screens.Config.f_muscles import *
from json import *

def _m_selector():
    for widget in f_selector.winfo_children():
        widget.destroy() 

    with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
        md = load(f)

    c = 1
    objects=["Empty"]#Says empty so appending starts at 1
    for i in md:
        if md[i] == False:
            ob = Selector(f_selector,i)
            
            objects.append(ob)

            objects[c].frame.grid(column=1,row=c,sticky=(E, W))
            
            f_selector.rowconfigure(c,weight=1)
            c+=1

def _m_muscles():
    for widget in f_muscles.winfo_children():
        widget.destroy() 

    with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
        md = load(f)

    c = 1
    objects=["Empty"]#Says empty so appending starts at 1
    for i in md:
        if md[i] == True:
            ob = Muscle(f_muscles,i)
            
            objects.append(ob)

            objects[c].frame.grid(column=1,row=c,sticky=(E, W))
            
            f_muscles.rowconfigure(c,weight=1)
            c+=1

class Muscle():
        """Each item in the menu is created from the corresponding .json file
        """
        def __init__(self,root,muscle,*args,**kwargs):
            self.frame = ttk.Frame(root,height=50,padding=10)
            self.frame.columnconfigure(1,weight=1)
            self.frame.columnconfigure(2,weight=1)
            self.frame.columnconfigure(3,weight=1)
            self.frame.rowconfigure(1,weight=1)

            self.label = ttk.Label(self.frame, text=muscle,justify="right")
            self.label.grid(column=1,row=1,sticky=(N, S, E, W))

            self.button = ttk.Button(self.frame, text = "Remove from Plan", *args, **kwargs)
            self.button.grid(column=2,row=1,sticky=(N, S, E, W))

            self.rest = StringVar(value="0")
            self.config = ttk.Entry(self.frame,textvariable=self.rest)
            self.config.grid(column=3,row=1,sticky=(N, S, E, W))

            self.root = root
            self.muscle = muscle
            self.button.config(command = self.select)

        def select(self):
            self.frame.destroy()
            with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
                md = load(f)
            md[self.muscle]=False
            with open("../TrainingApp/Screens/Config/Menus/selected.json","w") as f:
                dump(md, f, indent =2)
            _m_selector()
            _m_muscles()

class Selector():
        """Each item in the menu is created from the corresponding .json file
        """
        def __init__(self,root,muscle,*args,**kwargs):
            self.frame = ttk.Frame(root,height=50,padding=10)
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
            self.frame.destroy()
            with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
                md = load(f)
            md[self.muscle]=True
            with open("../TrainingApp/Screens/Config/Menus/selected.json","w") as f:
                dump(md, f, indent =2)
            _m_selector()
            _m_muscles()