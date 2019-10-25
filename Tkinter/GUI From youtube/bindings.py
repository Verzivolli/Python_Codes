# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:46:37 2019

@author: C.R.C
"""

from tkinter import *

# create window object
root = Tk()

def leftClick(event):
    print('Left')
def rightClick(event):
    print('Right')
def scroll(event):
    print('Scroll')
def leftKey(event):
    print('leftKey')
def rightKey(event):
    print('rightKey')
## placing a button (widget)
# creating the button

root.geometry("500x500")

root.bind('<Button-1>', leftClick)
root.bind('<Button-2>', scroll)
root.bind('<Button-3>', rightClick)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
# may bind as many function as we want to any widget


# loop window to keep it open otherwise it will close as soon as it is created
# mainloop() will keep the program (window) running until x is clicked
root.mainloop()