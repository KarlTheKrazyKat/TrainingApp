#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
from Screens.Config.f_selector import *
#File Specific Imports
from json import *
from modules.selector import Selector

def _m_selector():
    with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
        md = load(f)

    c = 1
    objects=["Empty"]#Says empty so appending starts at 1
    for i in md:
        if md[i] == False:
            ob = Selector(f_selector,i)
            
            objects.append(ob)

            objects[c].frame.grid(column=1,row=c,sticky=(N, S, E, W))
            
            f_selector.rowconfigure(c,weight=1)
            c+=1