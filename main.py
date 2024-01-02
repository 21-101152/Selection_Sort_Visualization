from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, END
import time
from rectangle import Rectangle


def on_enter_pressed(event):
    add_number()

def on_entry_focus(event):
    entry_frame.config(borderwidth=2, relief="solid")

def on_entry_focusout(event):
    entry_frame.config(borderwidth=1)

def create_text_once(marginx, marginy, my_text, my_font):
    global no_more_elements
    if not hasattr(create_text_once, "_called"):
        no_more_elements = canvas.create_text(
            marginx,
            marginy,
            text = my_text,
            font = my_font
        )
        create_text_once._called = True
        
def delete_element(item_id):
    canvas.delete(item_id)

array_rectangles = []

def set_initial_arrtibutes_rectangle():
    Rectangle.xleft = 20
    Rectangle.xright = Rectangle.xleft+40
    Rectangle.ydown = 289
    Rectangle.yup = 329
    Rectangle.index = 1

def clear_button_clicked():
    for i in range (len(array_rectangles)):
        delete_element(array_rectangles[i].id)
        delete_element(array_rectangles[i].text_widget)
    array_rectangles.clear()
    set_initial_arrtibutes_rectangle()

def change_fill_color(item_id, new_color, duration):
    canvas.itemconfig(item_id, fill=new_color)
    window.update_idletasks()
    time.sleep(duration)

def add_number():
    global no_more_elements
    if len(array_rectangles) < 15:
        text = entry_1.get()
        array_rectangles.append(Rectangle(canvas, "LightGrey", "black", text))
    else:
        create_text_once(
            500,
            200,
            "You can't add more",
            ("Jost Bold", 12, "bold")
        )
    entry_1.delete(0, END)

def move_rectangle(rec, deltax, deltay):
    canvas.move(rec.id, deltax, deltay)
    canvas.move(rec.text_widget, deltax, deltay)
    window.update_idletasks()

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

def sort():
    delete_element(no_more_elements)
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

window.geometry("656x500")
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

button_style = {
    "background": "#000000",
    "foreground": "#FFFFFF",
    "font": ("Arial", 12, "bold"),
    "width": 26,
    "height": 2,
    "bd": 0,
    "highlightthickness": 0, 
    "relief": "flat",
    "borderwidth": 0,
}

AddButton = Button(
    window,
    text= "Add",
    command=lambda: add_number(),
    **button_style
)

AddButton.place(
    x=437.0,
    y=152.0,
    width=62.0,
    height=26.0
)


SortButton = Button(
    window,
    text = "Sort",
    command=lambda: sort(),
    **button_style
)

SortButton.place(
    x=280.0,
    y=200.0,
    width=70.0,
    height=30.0
)



ClearButton = Button(
    window,
    text="Clear",
    command=lambda: clear_button_clicked(),
    **button_style
)



ClearButton.place(
    x=504.0,
    y=152.0,
    width=62.0,
    height=26.0
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

no_more_elements = None

entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
entry_1.bind("<Return>", on_enter_pressed)
window.resizable(False, False)
window.mainloop()
