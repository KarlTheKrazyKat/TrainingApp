#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
from Screens.Config.f_muscles import *
#File Specific Imports
from json import *
from modules.muscle import Muscle

def _m_muscles():
    with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
        md = load(f)

    c = 1
    objects=["Empty"]#Says empty so appending starts at 1
    for i in md:
        if md[i] == True:
            ob = Muscle(f_muscles,i)
            
            objects.append(ob)

            objects[c].frame.grid(column=1,row=c,sticky=(N, S, E, W))
            
            f_muscles.rowconfigure(c,weight=1)
            c+=1