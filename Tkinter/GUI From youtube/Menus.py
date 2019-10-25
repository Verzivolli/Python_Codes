# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:53:19 2019

@author: Ani Verzivolli
"""

from tkinter import *

root = Tk()

def random():
    print('random function executed!')

mainMenu = Menu(root)
root.configure(menu = mainMenu)
# Menu is an accumulation of submenus
subMenu = Menu(mainMenu)

mainMenu.add_cascade(label = 'File', menu = subMenu)
subMenu.add_command(label = 'New File', command = random)
subMenu.add_command(label = 'Open', command = random)

subMenu.add_separator()
subMenu.add_command(label = 'Random function', command = random)


root.mainloop()