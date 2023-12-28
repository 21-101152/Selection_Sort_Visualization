
from pathlib import Path
from tkinter import Tk, Canvas
class Rectangle:
    xleft = 50
    xright = 90
    ydown = 289
    yup = 329
    def __init__ (self, canvas,fill_color, outline_color):
        self.canvas = canvas
        self.create_rectangle(fill_color, outline_color)
        Rectangle.xleft += 40
        Rectangle.xright += 40
        Rectangle.ydown += 40
        Rectangle.yup += 40
    
    def create_rectangle(self, fill_color, outline_color):
        self.canvas.create_rectangle(
        self.xleft,
        self.ydown,
        self.xright,
        self.yup,
        fill=fill_color,
        outline=outline_color
        )
        return self.canvas
        
