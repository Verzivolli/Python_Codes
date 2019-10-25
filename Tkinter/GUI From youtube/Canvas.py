# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:16:46 2019

@author: Ani Verzivolli
"""

from tkinter import *
import random
import time
tk = Tk()
## canvas for other parts
#canvas = Canvas(root, width = 300, height = 300)
#canvas.pack()

# canvas.create_rectangle(50,50,150,150)
# canvas.create_line(25,25,75,45)
# canvas.create_polygon(125,251,89,95,254,246,142,146)

## Random rectangles
#def randomRects(num):
#    for i in range(0, num):
#        x1 = random.randrange(300)
#        y1 = random.randrange(300)
#        x2 = random.randrange(300)
#        y2 = random.randrange(300)
#        canvas.create_rectangle(x1,y1,x2,y2)
## randomRects(150)

## Arcs (Elipses arcs)
#canvas.create_arc(10,10,200,80, extent = 46, style = ARC)
#canvas.create_arc(10,80,200,160, extent = 90, style = ARC)
#canvas.create_arc(10,80,200,160, extent = 359, style = ARC)

### Bounce
tk.title('Bounce!')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)# place the window in front of all other windows
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245, 100)
    
    def draw(self):
        self.canvas.move(self.id, 0, 1)

ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

root.mainloop()