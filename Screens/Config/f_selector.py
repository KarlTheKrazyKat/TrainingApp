#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
#File Specific Imports
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

#All in module