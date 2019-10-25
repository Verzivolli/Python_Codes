# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:22:42 2019

@author: Ani Verzivolli
"""

from tkinter import *

root = Tk()


equa = ""
equation = StringVar()

calculation = Label(root, textvariable = equation)

# equation.set('23+51')
equation.set('Enter your equation:')
calculation.grid(columnspan = 4)

# function to create number button
def btnpress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
def clear():
    global equa
    equa = ""
    equation.set('Enter your equation:')
def evaluation():
    global equa
    equa = str(eval(equa))
    equation.set(equa)
    
#Button0 = Button(root, text = "0", command = lambda:btnpress(0))
def createButton( text, param, row, col, rowspan = 1, colspan = 1):
    tmp_button_holder = Button(root, text = text, command = lambda:btnpress(param))
    tmp_button_holder.grid(row = row, column = col, rowspan = rowspan, columnspan = colspan)
    return tmp_button_holder
def createButtonF( text, func, row, col, rowspan = 1, colspan = 1):
    tmp_button_holder = Button(root, text = text, command = func)
    tmp_button_holder.grid(row = row, column = col, rowspan = rowspan, columnspan = colspan)
    return tmp_button_holder

Button1 = createButton("1", "1", 1, 0, 1, 1)
Button2 = createButton("2", "2", 1, 1, 1, 1)
Button3 = createButton("3", "3", 1, 2, 1, 1)
Button4 = createButton("4", "4", 2, 0, 1, 1)
Button5 = createButton("5", "5", 2, 1, 1, 1)
Button6 = createButton("6", "6", 2, 2, 1, 1)
Button7 = createButton("7", "7", 3, 0, 1, 1)
Button8 = createButton("8", "8", 3, 1, 1, 1)
Button9 = createButton("9", "9", 3, 2, 1, 1)
Button0 = createButton("0", "0", 4, 1, 1, 1)

plus = createButton("+", "+", 1, 3, 1, 1)
minus = createButton("-", "-", 2, 3, 1, 1)
divide = createButton("/", "/", 3, 3, 1, 1)
multipby = createButton("*", "*", 4, 3, 1, 1)
clear = createButtonF("C", clear, 4, 0, 1, 1)
evaluate = createButtonF("=", evaluation, 4, 2, 1, 1)

root.mainloop()