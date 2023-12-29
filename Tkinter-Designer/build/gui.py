
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

x1_now = 50.0
x2_now = 90.0
array = []
array_text = []
array_rectangles = []

def add_number():
    global x1_now, x2_now
    text = entry_1.get()
    array_rectangles.append(Rectangle(canvas, "LightGray", "black", text))
    entry_1.delete(0, END)
    x1_now += 40
    x2_now += 40

def create_array_element(num):
    canvas.create_text(
        x1_now + 20,
        309,
        text = num,
        font=("Jost Bold", 12, "bold")
    )

def sort():
    minElement = array_rectangles[0]
    minElement.update_rectangle_color("red")
    for i in range(1, len(array_rectangles)):
        for j in range(1, len(array_rectangles)+1):
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
#canvas.pack()
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

def move_rec(rec, n, dir):
    x1,  y1, x2, y2 = canvas.coords(rec.id)

    if move_rec.counter < 20:
        canvas.move(rec.id, 0, dir*5)
        move_rec.counter += 1

    elif dir > 0 and x1 < (88+(40*n)) :
        canvas.move(rec.id, dir*5, 0)

    elif dir < 0 and x1 > (88+(40*n)) :
        canvas.move(rec.id, dir*5, 0)    

    elif move_rec.counter < 40:
        canvas.move(rec.id, 0, -1*dir*5)
        move_rec.counter += 1

    if move_rec.counter < 40:
        window.after(35, move_rec, rec, n, dir)


def swap(minElement, toright, element, toleft):
    canvas.itemconfig(minElement, fill='red')
    canvas.itemconfig(element, fill='red')

    thread1 = threading.Thread(target=move_rec (element, toright, 1))
    thread2 = threading.Thread(target=move_rec (minElement, toleft, -1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


move_rec.counter = 0

entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
entry_1.bind("<Return>", on_enter_pressed)
window.resizable(False, False)
window.mainloop()
