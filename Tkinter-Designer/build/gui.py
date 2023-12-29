
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, END
import threading
import time
from rectangle import Rectangle

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\College\Junior\Algorithms\Selection_Sort_Visualization_Project\Selection_Sort_Visualization\Tkinter-Designer\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def on_enter_pressed(event):
    add_number()

def on_entry_focus(event):
    entry_frame.config(borderwidth=2, relief="solid")

def on_entry_focusout(event):
    entry_frame.config(borderwidth=1)

array_rectangles = []

def add_number():
    text = entry_1.get()
    array_rectangles.append(Rectangle(canvas, "LightGray", "black", text))
    entry_1.delete(0, END)

def move_rectangle(rec, deltax, deltay):
    canvas.move(rec.id, deltax, deltay)
    canvas.move(rec.text_widget, deltax, deltay)

def sort():
    min_idx = 0
    canvas.itemconfig(array_rectangles[min_idx].id, fill = "red")
    for i in range(0, len(array_rectangles)):
        for j in range(i+1, len(array_rectangles)):
            window.after(15, lambda: canvas.itemconfig(array_rectangles[j].id, fill='Grey'))
            window.after(15, lambda: canvas.itemconfig(array_rectangles[j-1].id, fill='LightGrey'))
            if array_rectangles[j].value < array_rectangles[min_idx].value:
                min_idx = j
            if (j == len(array_rectangles) - 1): window.after(15, lambda: canvas.itemconfig(array_rectangles[j].id, fill='LightGrey'))
        if (i != min_idx): swap(array_rectangles[min_idx], array_rectangles[i], (min_idx-i)*40)
        temp = array_rectangles[i]
        array_rectangles[i] = array_rectangles[min_idx]
        array_rectangles[min_idx] = temp
        
window = Tk()
window.title("Selection Sort Visualization")

window.geometry("656x467")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 467,
    width = 656,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

canvas.create_rectangle(0.0, 0.0, 656.0, 67.0, fill = "#833F3F", outline = "")

canvas.create_text(
    76.0,
    11.0,
    anchor="nw",
    text="Selection Sort Visualization",
    fill="#FFFFFF",
    font=("Inter Black", 36 * -1)
)


AddButton_image = PhotoImage(
    file=relative_to_assets("AddButton.png"))
AddButton = Button(
    image=AddButton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_number(),
    relief="raised"
)

AddButton.place(
    x=437.0,
    y=152.0,
    width=62.0,
    height=26.0
)

SortButton_image = PhotoImage(
    file=relative_to_assets("SortButton.png"))
SortButton = Button(
    image= SortButton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sort(),
    relief="raised"
)

SortButton.place(
    x=280.0,
    y=224.0,
    width=95.0,
    height=40.0
)


entry_frame = Frame(window, borderwidth=1, bg = "#000000")
entry_frame.place(
    x=156.0,
    y=145.0,
    width=256.0,
    height=30.0
)

entry_1 = Entry(
    entry_frame,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    relief = "ridge"
)

def move_rec_up(rec, vertical):
    if vertical > 0:
        move_rectangle(rec, 0, 1)
        window.after(10, move_rec_up, rec, vertical - 1)

def move_rec_down(rec, vertical):
    if vertical > 0:
        move_rectangle(rec, 0, -1)
        window.after(10, move_rec_down, rec, vertical - 1)

def move_rec_right(rec, distance):
    if distance > 0:
        move_rectangle(rec, 1, 0)
        window.after(10, move_rec_right, rec, distance - 1)

def move_rec_left(rec, distance):
    if distance > 0:
        move_rectangle(rec, -1, 0)
        window.after(10, move_rec_left, rec, distance - 1)

def swap(minElement, element, distance):

    canvas.itemconfig(minElement.id, fill='red')
    canvas.itemconfig(element.id, fill='red')
    move_rec_down(element, 50)
    move_rec_right(element, distance)
    move_rec_up(element, 50)
    canvas.itemconfig(element, fill='LightGrey')
    move_rec_up(minElement, 50)
    move_rec_left(minElement, distance)
    move_rec_down(minElement, 50)
    canvas.itemconfig(minElement, fill='LightGrey')

entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
entry_1.bind("<Return>", on_enter_pressed)
window.resizable(False, False)
window.mainloop()
