#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
#File Specific Imports
import subprocess

#Create Frame
f_main = ttk.Frame(root,height=60,width=200,relief='sunken')
f_main.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=(N, S, E, W))

#Configure Frame Grid
f_main.columnconfigure(1,weight=1)
f_main.columnconfigure(2,weight=1)
f_main.rowconfigure(1,weight=1)

#Declare Stringvars

#Button Commands and Functions
def open():
    print("Gonna do some subwindow bullshit - add to VIS extension first")

def new():
    root.destroy()
    subprocess.call("python Config.py")

#Navigation

#########################
#####Visual Elements#####
#########################

#Open Button
vb_open = ttk.Button(f_main, text="Open Project", command=open,padding=50)
vb_open.grid(row=1,column=1,sticky=(N, S, E, W))

#New Button
vb_new = ttk.Button(f_main, text="New Project", command=new,padding=50)
vb_new.grid(row=1,column=2,sticky=(N, S, E, W))