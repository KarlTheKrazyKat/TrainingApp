#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
#File Specific Imports
from json import *
from modules.Config.m_selector import _m_selector, _m_muscles

#Create Frame
f_controls = ttk.Frame(root,height=150,width=200,relief='sunken',padding=25)
f_controls.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=(N, S, E, W))

#Configure Frame Grid
f_controls.columnconfigure(1,weight=1)
f_controls.columnconfigure(2,weight=1)
f_controls.rowconfigure(1,weight=1)
f_controls.rowconfigure(2,weight=4)

#Declare Stringvars
muscname = StringVar()

#Button Commands and Functions
def findAll():
    print("Will search in all plans and load all muscles")

def newMusc():
    with open("../TrainingApp/Screens/Config/Menus/selected.json","r") as f:
        md = load(f)
    md[muscname.get()]=False
    with open("../TrainingApp/Screens/Config/Menus/selected.json","w") as f:
                dump(md, f, indent =2)
    _m_selector()
    _m_muscles()
    print("Will create a new musc element called ",muscname.get())

#Navigation

#########################
#####Visual Elements#####
#########################

#Find Muscles
vb_find = ttk.Button(f_controls, text="Find Muscles", command=findAll)
vb_find.grid(row=2,column=1,sticky=(N, S, E, W))

#New Muscle Name Entry
ve_name = ttk.Entry(f_controls, textvariable=muscname)
ve_name.grid(row=1,column=1,columnspan=2,sticky=(N, S, E, W))

#New Muscle
vb_new = ttk.Button(f_controls, text="Create Muscle", command=newMusc)
vb_new.grid(row=2,column=2,sticky=(N, S, E, W))