# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:09:22 2019

@author: C.R.C
"""

from tkinter import *

# create window object
window = Tk()

def km_to_miles():
    #print(e1_value.get())
    ##on insert END will place the text at the end of existing text
    #t1.insert(END, e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

## placing a button (widget)
# creating the button
b1 = Button(window, text = 'click', command = km_to_miles)
# placing button to window
b1.grid(row = 0, column = 0)#, rowspan = 2)
# can also use b1.pack() but doesnt give options for positioning

# Entering entry widged
# Entry variable holder
e1_value = StringVar()
# creating entry widget
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0, column= 1)

# entering text widget
t1 = Text(window, height = 2, width = 25) # default size is very big
t1.grid(row=0, column= 2)



# loop window to keep it open otherwise it will close as soon as it is created
# mainloop() will keep the program (window) running until x is clicked
window.mainloop()