# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:25:54 2019

@author: C.R.C
"""

from tkinter import *

# create window object
root = Tk()

label1 = Label(root, text = 'Name:')
label1.grid(row = 0, column = 0, sticky ="E")
label2 = Label(root, text = 'Pasword:')
label2.grid(row = 1, column = 0, sticky ="E")
label1 = Label(root, text = 'Label1')

entrySpace = Entry(root)
entrySpace.grid(row = 0, column = 1)

entrySpace2 = Entry(root)
entrySpace2.grid(row = 1, column = 1)

cbutton = Checkbutton(root, text = 'Remember password')
cbutton.grid(columnspan = 2)

# loop window to keep it open otherwise it will close as soon as it is created
# mainloop() will keep the program (window) running until x is clicked
root.mainloop()