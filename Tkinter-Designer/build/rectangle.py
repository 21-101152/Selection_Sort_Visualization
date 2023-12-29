
from pathlib import Path
from tkinter import Tk, Canvas
class Rectangle:
    xleft = 50
    xright = 90
    ydown = 289
    yup = 329
    def __init__ (self, canvas, fill_color, outline_color, text):
        self.canvas = canvas
        self.text = text
        self.value = int(text)
        self.fill_color = fill_color
        self.outline_color = outline_color
        self.id = self.create_rectangle()
        Rectangle.xleft += 40
        Rectangle.xright += 40
    
    def create_rectangle(self):
        rec = self.canvas.create_rectangle(
        self.xleft,
        self.ydown,
        self.xright,
        self.yup,
        fill=self.fill_color,
        outline=self.outline_color
        )
        self.canvas.create_text(
        self.xleft + 20,
        309,
        text = self.text,
        font=("Jost Bold", 12, "bold")
        )
        return rec
    
    def update_rectangle_color(self, new_color):
        self.canvas.itemconfig(self, fill = new_color)

    def canvas_get(self):
        return self.canvas
        
        
