from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, END
from tkinter import ttk
import time
from rectangle import Rectangle


def on_enter_pressed(event):
    add_number()

def on_entry_focus(event):
    entry_frame.config(borderwidth=2, relief="solid")

def on_entry_focusout(event):
    entry_frame.config(borderwidth=1)

def on_sort_selection(event):
    pass  

def on_sort_button_click():
    selected_sort = sort_options.get()
    delete_element(no_more_elements)
    if selected_sort == "Insertion Sort":
        clarification(selected_sort)
        insertion_sort()
    elif selected_sort == "Selection Sort":
        clarification(selected_sort)
        selection_sort()

def create_circle(marginx, color):
    circle = canvas.create_oval(marginx - 7.5, 395, marginx + 7.5, 410 , fill=color)
    return circle

def delete_clarifications():
    delete_element(redCircleText)
    delete_element(redCircle)
    delete_element(greyCircleText)
    delete_element(greyCircle)
    delete_element(greenCircleText)
    delete_element(greenCircle)

def clarification(type):
    global redCircle, greenCircle, greyCircle, redCircleText, greenCircleText, greyCircleText
    if type == "Selection Sort":
        delete_clarifications()
        redCircle = create_circle(52.5 ,"red")
        redCircleText = canvas.create_text(
            120.0,
            402.5,
            text="Min element",
            font = ("Jost Bold", 12, "bold")
        )
        greyCircle = create_circle(242.5, "Grey")
        greyCircleText = canvas.create_text(
            320.0,
            402.5,
            text="Current element",
            font = ("Jost Bold", 12, "bold")
        )
        greenCircle = create_circle(442.5, "Green")
        greenCircleText = canvas.create_text(
            529.0,
            402.5,
            text="Sorted subarray",
            font = ("Jost Bold", 12, "bold")
        )
    elif type == "Insertion Sort":
        delete_clarifications()
        redCircle = create_circle(52.5 ,"red")
        redCircleText = canvas.create_text(
            130.0,
            402.5,
            text="Element to insert",
            font = ("Jost Bold", 12, "bold")
        )
        greyCircle = create_circle(242.5, "Grey")
        greyCircleText = canvas.create_text(
            320.0,
            402.5,
            text="Current   Element",
            font = ("Jost Bold", 12, "bold")
        )
        greenCircle = create_circle(442.5, "Green")
        greenCircleText = canvas.create_text(
            545.0,
            402.5,
            text="Sorted subarray till now",
            font = ("Jost Bold", 12, "bold")
        )



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
        delete_clarifications()
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
    move_rec_down(element, 50)
    move_rec_right(element, distance)
    move_rec_up(element, 50)
    change_fill_color(element.id, 'LightGrey', 0.25)
    move_rec_up(minElement, 50)
    move_rec_left(minElement, distance)
    move_rec_down(minElement, 50)
    change_fill_color(minElement.id, 'LightGrey', 0.25)

def selection_sort():
    min_idx = 0
    change_fill_color(array_rectangles[min_idx].id, 'red', 0.25)
    for i in range(0, len(array_rectangles)-1):
        min_idx = i
        change_fill_color(array_rectangles[min_idx].id, 'red', 0.25)
        for j in range(i, len(array_rectangles)):
            
            if (j-1 != min_idx) and (j != i):
                change_fill_color(array_rectangles[j-1].id, 'LightGrey', 0.25) 
                time.sleep(0.2)
            if (j != min_idx):
                change_fill_color(array_rectangles[j].id, 'Grey', 0.25)
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
        change_fill_color(array_rectangles[i].id, 'Green', 0.25)
    change_fill_color(array_rectangles[-1].id, 'Green', 0.25)


def insertion_sort():
    for i in range(1, len(array_rectangles)):
        key = i
        j = i - 1
        change_fill_color(array_rectangles[key].id, 'red', 0.25)
        while j >= 0 and array_rectangles[key].value < array_rectangles[j].value:
            if (j == i - 1):
                time.sleep(0.5)
                for k in range (0, j+1):
                    change_fill_color(array_rectangles[k].id, 'LightGrey', 0)
            change_fill_color(array_rectangles[key].id, 'red', 0.25)
            change_fill_color(array_rectangles[j].id, 'Grey', 0.25)
            time.sleep(0.1)
            swap(array_rectangles[j+1], array_rectangles[j], 40)
            change_fill_color(array_rectangles[j+1].id, 'LightGrey', 0.25)
            array_rectangles[j], array_rectangles[j+1] = array_rectangles[j+1], array_rectangles[j]
            j -= 1
            key = j + 1
            window.update_idletasks()
            time.sleep(0.1)
        for k in range (0, i+1):
            change_fill_color(array_rectangles[k].id, 'Green', 0)
        time.sleep(0.5)

   
        
window = Tk()
window.title("Sort Visualization")



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
    200.0,
    11.0,
    anchor="nw",
    text="Sort Visualization",
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



window.geometry("656x500")
window.configure(bg = "#FFFFFF")
sort_options = ttk.Combobox(window, values=["Insertion Sort", "Selection Sort"])
sort_options.current(0)
sort_options.place(x=100.0, y=200.0, width=120.0, height=30.0)
sort_options.bind("<<ComboboxSelected>>", on_sort_selection)

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
    command=on_sort_button_click,
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
redCircle= None
greenCircle= None
greyCircle= None
redCircleText = None
greyCircleText = None
greenCircleText = None


entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
entry_1.bind("<Return>", on_enter_pressed)
window.resizable(False, False)
window.mainloop()
