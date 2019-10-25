# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:29:12 2019

@author: Ani Verzivolli
"""

from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
msgbox.showinfo("Window Title","Did you know the world just blew up?")

answer = msgbox.askquestion("Question1", "Are you a human?")
if answer == "yes":
    msgbox.showinfo("Window Title","Me too. The worl is small isn't it?")
elif answer == "no":
    msgbox.showinfo("Alien", "Alien confirmed")

root.mainloop()