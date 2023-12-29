import tkinter as tk
import threading


def move_rec(rec, n, dir):
    x1, y1, x2, y2 = canvas.coords(rec)

    if move_rec.counter < 20:
        canvas.move(rec, 0, dir*5)
        move_rec.counter += 1

    elif dir > 0 and x1 < (88+(40*n)) :
        canvas.move(rec, dir*5, 0)

    elif dir < 0 and x1 > (88+(40*n)) :
        canvas.move(rec, dir*5, 0)    

    elif move_rec.counter < 40:
        canvas.move(rec, 0, -1*dir*5)
        move_rec.counter += 1

    if move_rec.counter < 40:
        root.after(35, move_rec, rec, n, dir)

def swap(x, indx, y, n):
    canvas.itemconfig(x, fill='red')
    canvas.itemconfig(y, fill='red')
    thread1 = threading.Thread(target=move_rec(y, indx, 1))
    thread2 = threading.Thread(target=move_rec(x, n, -1))
 
# Start the threads
    thread1.start()
    thread2.start()

# Wait for both threads to finish
    thread1.join()
    thread2.join()


root = tk.Tk()
root.title("Simple Animation")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()
a = canvas.create_rectangle(128.0, 289.0, 168.0, 329.0, fill='blue')
b = canvas.create_rectangle(168.0, 289.0, 208.0, 329.0, fill='blue')
c = canvas.create_rectangle(208.0, 289.0, 248.0, 329.0, fill='blue')
d = canvas.create_rectangle(248.0, 289.0, 288.0, 329.0, fill='blue')
f = canvas.create_rectangle(288.0, 289.0, 328.0, 329.0, fill='blue')
print (d)
rec = canvas.create_rectangle(
    328.0, 289.0, 368.0, 329.0, fill='blue')


move_rec.counter = 0

swap(d, 4, b, 2)

root.mainloop()
