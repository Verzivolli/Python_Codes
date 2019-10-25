# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:35:32 2019

@author: C.R.C
"""

from tkinter import *

# create window object
window = Tk()

def printName():
    print('Hello there!')

## placing a button (widget)
# creating the button

# can also use b1.pack() but doesnt give options for positioning


## placing a button (widget)
# creating the button
b2 = Button(window, text = 'Button 2!')
b2.bind("<Button-1>",printName)# if event left mouse is cliced
# placing button to window
b2.pack()#, rowspan = 2)
# can also use b1.pack() but doesnt give options for positioning


# loop window to keep it open otherwise it will close as soon as it is created
# mainloop() will keep the program (window) running until x is clicked
window.mainloop()