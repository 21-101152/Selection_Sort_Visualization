import tkinter as tk
import threading
import time

def move_rec(rec, n, dir):
    x1, y1, x2, y2 = canvas.coords(rec)

    for _ in range(20):
        canvas.move(rec, 0, dir * 2.5)
        root.update()  # Update the GUI to visually move the rectangle
        time.sleep(0.03)  # Adjust the sleep duration for a smooth animation

    if x1 < (88 + (40 * n)):
        for _ in range(20):
            canvas.move(rec, dir * 2.5, 0)
            root.update()
            time.sleep(0.03)

    for _ in range(20):
        canvas.move(rec, 0, -1 * dir * 2.5)
        root.update()
        time.sleep(0.03)

# Other parts of your code remain unchanged

def swap(x, indx, y, n):
    canvas.itemconfig(x, fill='red')
    canvas.itemconfig(y, fill='red')

    thread = threading.Thread(target=move_rec, args=(y, indx, 1))
    thread.start()

    move_rec(x, n, -1)  # Run the second move_rec directly without threading

root = tk.Tk()
root.title("Simple Animation")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()
a = canvas.create_rectangle(128.0, 289.0, 168.0, 329.0, fill='blue')
b = canvas.create_rectangle(168.0, 289.0, 208.0, 329.0, fill='blue')
c = canvas.create_rectangle(208.0, 289.0, 248.0, 329.0, fill='blue')
d = canvas.create_rectangle(248.0, 289.0, 288.0, 329.0, fill='blue')
f = canvas.create_rectangle(288.0, 289.0, 328.0, 329.0, fill='blue')

# ... (rest of your code)

# Set an initial counter value for the move_rec function
move_rec.counter = 0

# Call the swap function to start the animation
swap(d, 4, b, 2)

root.mainloop()
