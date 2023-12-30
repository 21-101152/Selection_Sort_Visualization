
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

def change_fill_color(item_id, new_color, duration):
    canvas.itemconfig(item_id, fill=new_color)
    window.update_idletasks()
    time.sleep(duration)

def add_number():
    text = entry_1.get()
    array_rectangles.append(Rectangle(canvas, "LightGrey", "black", text))
    entry_1.delete(0, END)

def move_rectangle(rec, deltax, deltay):
    canvas.move(rec.id, deltax, deltay)
    canvas.move(rec.text_widget, deltax, deltay)
    window.update_idletasks()

def sort():
    min_idx = 0
    change_fill_color(array_rectangles[min_idx].id, 'red', 0.25)
    for i in range(0, len(array_rectangles)-1):
        min_idx = i
        change_fill_color(array_rectangles[min_idx].id, 'red', 0.25)
        for j in range(i, len(array_rectangles)):
            if (j != min_idx): 
                change_fill_color(array_rectangles[j].id, 'Grey', 0.1)
                time.sleep(0.2)
            if (j-1 != min_idx):
                change_fill_color(array_rectangles[j-1].id, 'LightGrey', 0.1)
                time.sleep(0.2)
            if array_rectangles[j].value < array_rectangles[min_idx].value:
                change_fill_color(array_rectangles[min_idx].id, 'LightGrey', 0.25)
                time.sleep(0.2)
                min_idx = j
                change_fill_color(array_rectangles[min_idx].id, 'red', 0.25)
                time.sleep(0.2)
            if (j == len(array_rectangles) - 1) and (j != min_idx): 
                change_fill_color(array_rectangles[j].id, 'LightGrey', 0.25)
                time.sleep(0.2)
        if (i < min_idx):
            swap(array_rectangles[min_idx], array_rectangles[i], (min_idx-i)*40)
            array_rectangles[i], array_rectangles[min_idx] = array_rectangles[min_idx], array_rectangles[i]
        else:
            change_fill_color(array_rectangles[min_idx].id, 'LightGrey', 0.25)
            time.sleep(0.25)
       
        
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
    for _ in range (vertical):
        move_rectangle(rec, 0, 1)
        window.update_idletasks()
        time.sleep(0.001)
    time.sleep(0.1)

def move_rec_down(rec, vertical):
    for _ in range (vertical):
        move_rectangle(rec, 0, -1)
        window.update_idletasks()
        time.sleep(0.001)
    time.sleep(0.1)

def move_rec_right(rec, distance):
    for _ in range (distance):
        move_rectangle(rec, 1, 0)
        window.update_idletasks()
        time.sleep(0.001)
    time.sleep(0.1)

def move_rec_left(rec, distance):
    for _ in range (distance):
        move_rectangle(rec, -1, 0)
        window.update_idletasks()
        time.sleep(0.001)
    time.sleep(0.1)

def swap(minElement, element, distance):

    change_fill_color(minElement.id, 'red', 0.25)
    change_fill_color(element.id, 'red', 0.25)
    move_rec_down(element, 50)
    move_rec_right(element, distance)
    move_rec_up(element, 50)
    change_fill_color(element.id, 'LightGrey', 0.25)
    move_rec_up(minElement, 50)
    move_rec_left(minElement, distance)
    move_rec_down(minElement, 50)
    change_fill_color(minElement.id, 'LightGrey', 0.25)

entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
entry_1.bind("<Return>", on_enter_pressed)
window.resizable(False, False)
window.mainloop()
