from tkinter import *
from tkinter import ttk
import sys

cfp="Win"

root = Tk()
root.title('New VIS Project')


def do_focus(event=None):
    x,y = root.winfo_pointerxy()
    root.winfo_containing(x,y).focus()

root.bind("<1>", do_focus)
