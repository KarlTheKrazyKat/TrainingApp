#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
import sys
#File Specific Imports
import time

#Configure Screen
print(cfp)

w = 1080
h = 720
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Configure Plan")
root.minsize(1080,720)
#root.iconbitmap("L:/WOM/PYWOM/Images/Icons/<some_icon>")

#Screen Elements
from Screens.Config.f_controls import *
from Screens.Config.f_muscles import *
from Screens.Config.f_selector import *

#Screen Grid
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=5)

#Screen Modules
from modules.Config.m_controls import *
from modules.Config.m_muscles import _m_muscles
from modules.Config.m_selector import _m_selector

#Handle Arguments

#Define Loop Modules

with open("../TrainingApp/muscles.cfg","r") as f:
    muscles = [line.strip() for line in f]

md = {}
for i in muscles:
    md[i]=False

with open("../TrainingApp/Screens/Config/Menus/selected.json","w") as f:
    dump(md, f, indent =2)

def loop():
    #screen modules run here
    _m_selector()
    _m_muscles()
    time.sleep(0.2)
    1+1

#Update Loop
while root.winfo_exists:
    loop()
    root.update()