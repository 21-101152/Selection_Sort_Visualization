
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, END
import threading
import time
from rectangle import Rectangle

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amare\Downloads\Tkinter-Designer-master\Tkinter-Designer\build\assets\frame0")


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
    minElement = array_rectangles[0]
    canvas.itemconfig(minElement.id, fill = "red")
    for i in range(1, len(array_rectangles)):
        for j in range(i, len(array_rectangles)):
            if array_rectangles[j-1].value < minElement.value:
                minElement =  array_rectangles[j-1]
                canvas.itemconfig(minElement.id, fill = "red")
                canvas.itemconfig(array_rectangles[j-1].id, fill = "LightGrey")
                index = j
        if (i != index): swap(minElement, index, array_rectangles[i-1], i)

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

def move_rec_right(y, indx):
    x1, y1, x2, y2 = canvas.coords(y.id)
    # Move down for the first 20 iterations
    if move_rec_right.counter < 20:
        move_rectangle(y, 0, -2)
        move_rec_right.counter += 1
    # Move left for the next 20 iterations
    elif x1 < (50+(40*(indx-y.index))):
        move_rectangle(y, 2, 0)
    # Move down the next 20 iterations
    elif move_rec_right.counter < 40:
        move_rectangle(y, 0, 2)
        move_rec_right.counter += 1

    if move_rec_right.counter < 40:
        window.after(40, move_rec_right, y, indx)

    if move_rec_right.counter >= 40:
        move_rec_right.counter = 0

def move_rec_left(x, n):
    x1, y1, x2, y2 = canvas.coords(x.id)
    # Move up for the first 20 iterations
    if move_rec_left.counter < 20:
        move_rectangle(x, 0, 2)
        move_rec_left.counter += 1
    # Move left for the next 20 iterations
    elif x1 > (50+(40*n)):
        move_rectangle(x, -2, 0)
    # Move down the next 20 iterations
    elif move_rec_left.counter < 40:
        move_rectangle(x, 0, -2)
        move_rec_left.counter += 1

    # else:
        # Reset the counter and move back to the original position
        # move_circle.counter = 0
        # canvas.move(circle, 2, -2)

    # move_rec_left.counter += 1
    if move_rec_left.counter < 40:
        window.after(40, move_rec_left, x, n)
    
    if move_rec_left.counter >= 40:
        move_rec_left.counter = 0

""" def move_rec(rec, n, dir):
    x1,  y1, x2, y2 = canvas.coords(rec.id)

    if move_rec.counter < 20:
        canvas.move(rec.id, 0, dir*5)
        move_rec.counter += 1

    elif dir > 0 and x1 != (50+(40*(n-1))):
        canvas.move(rec.id, dir*5, 0)

    elif dir < 0  and x1 != (50+(40*(rec.id-1))):
        canvas.move(rec.id, dir*5, 0)    

    elif move_rec.counter < 40:
        canvas.move(rec.id, 0, -1*dir*5)
        move_rec.counter += 1

    if move_rec.counter < 40:
        window.after(35, move_rec, rec, n, dir)
    
    if move_rec.counter >= 40:
        move_rec.counter = 0 """


def swap(minElement, toright, element, toleft):
    canvas.itemconfig(minElement, fill='red')
    canvas.itemconfig(element, fill='red')

    thread1 = threading.Thread(target=move_rec_right(element, toright))
    thread2 = threading.Thread(target=move_rec_left (minElement, toleft))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    canvas.itemconfig(minElement, fill='LightGrey')
    canvas.itemconfig(element, fill='LightGrey')

move_rec_right.counter = 0
move_rec_left.counter = 0

entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
entry_1.bind("<Return>", on_enter_pressed)
window.resizable(False, False)
window.mainloop()
