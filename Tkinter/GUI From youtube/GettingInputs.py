# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:17:36 2019

@author: C.R.C
"""

from tkinter import *

root = Tk()

label1 = Label(root, text = "Enter your expression:")
label1.pack()

def evaluate(event):
    data = e.get()
    ans.configure(text = "Answer: " + str(eval(data)))

e = Entry(root)

e.bind("<Return>", evaluate) # in mac
e.bind("<Enter>", evaluate) # in windows
e.pack()
ans = Label(root)
ans.pack()

root.mainloop()