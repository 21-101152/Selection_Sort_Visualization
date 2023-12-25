
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, END


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amare\Downloads\Tkinter-Designer-master\Tkinter-Designer\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def on_entry_focus(event):
    entry_frame.config(borderwidth=2, relief="solid")

def on_entry_focusout(event):
    entry_frame.config(borderwidth=1)
x1_now = 50.0
x2_now = 90.0
def add_number(num):
    global x1_now, x2_now
    text = entry_1.get()
    create_rectangle(x1_now, 289.0, x2_now, 329.0, "#D9D9D9", "black")
    create_text(text)
    entry_1.delete(0, END)
    x1_now += 40
    x2_now += 40

def create_rectangle(x1, y1, x2, y2, fill_color, outline_color):
    canvas.create_rectangle(
    x1,
    y1,
    x2,
    y2,
    fill=fill_color,
    outline=outline_color)

def create_text(num):
    canvas.create_text(
        x1_now + 20,
        309,
        text = num
    )


window = Tk()

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

create_rectangle(0.0, 0.0, 656.0, 67.0, "#833F3F", "")
""" create_rectangle(128.0, 289.0, 168.0, 329.0, "#D9D9D9","black")
create_rectangle(168.0, 289.0, 208.0, 329.0, "#D9D9D9", "black")
create_rectangle(208.0, 289.0, 248.0, 329.0, "#D9D9D9", "black")
create_rectangle(248.0, 289.0, 288.0, 329.0, "#D9D9D9", "black")
create_rectangle(288.0, 289.0, 328.0, 329.0, "#D9D9D9", "black")
create_rectangle(328.0, 289.0, 368.0, 329.0, "#D9D9D9", "black")
create_rectangle(368.0, 289.0, 408.0, 329.0, "#D9D9D9", "black")
create_rectangle(408.0, 289.0, 448.0, 329.0, "#D9D9D9", "black")
create_rectangle(448.0, 289.0, 488.0, 329.0, "#D9D9D9", "black")
create_rectangle(488.0, 289.0, 528.0, 329.0, "#D9D9D9", "black") """










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
    command=lambda: add_number("5"),
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
    command=lambda: print("SortButton clicked"),
    relief="raised"
)
SortButton.place(
    x=280.0,
    y=224.0,
    width=95.0,
    height=40.0
)

""" entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    284.0,
    165.0,
    image=entry_image_1
) """

entry_frame = Frame(window, borderwidth=1, bg = "#000000")
#entry_frame.pack(padx=156, pady=155)
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

entry_1.pack(fill="both", expand=True)
entry_1.bind("<FocusIn>", on_entry_focus)
entry_1.bind("<FocusOut>", on_entry_focusout)
window.resizable(False, False)
window.mainloop()
