#Default Imports
from tkinter import *
from tkinter import ttk
from Screens.root import *
import sys
#File Specific Imports

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
from modules.Config.m_muscles import *
from modules.Config.m_selector import *

#Handle Arguments

#Define Loop Modules
def loop():
    #screen modules run here
    1+1

#Update Loop
while root.winfo_exists:
    loop()
    root.update()