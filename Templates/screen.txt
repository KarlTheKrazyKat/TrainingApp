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
root.title("Placeholder Title")
root.minsize(1080,720)
#root.iconbitmap("L:/WOM/PYWOM/Images/Icons/<some_icon>")

#Screen Elements

#Screen Grid
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

#Screen Modules

#Handle Arguments

#Define Loop Modules
def loop():
    #screen modules run here
    1+1

#Update Loop
while root.winfo_exists:
    loop()
    root.update()