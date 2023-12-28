import tkinter as tk
import threading


def move_rec_right(y, indx):
    x1, y1, x2, y2 = canvas.coords(y)
    # Move down for the first 20 iterations
    if move_rec_right.counter < 20:
        canvas.move(y, 0, 2)
        move_rec_right.counter += 1
    # Move left for the next 20 iterations
    elif x1 < (88+(40*indx)):
        canvas.move(y, 2, 0)
    # Move down the next 20 iterations
    elif move_rec_right.counter < 40:
        canvas.move(y, 0, -2)
        move_rec_right.counter += 1

    # else:
        # Reset the counter and move back to the original position
        # move_circle.counter = 0
        # canvas.move(circle, 2, -2)

   # move_rec_left.counter += 1
    if move_rec_right.counter < 40:
        root.after(40, move_rec_right, y, indx)


def move_rec_left(x, n):
    x1, y1, x2, y2 = canvas.coords(x)
    # Move up for the first 20 iterations
    if move_rec_left.counter < 20:
        canvas.move(x, 0, -2)
        move_rec_left.counter += 1
    # Move left for the next 20 iterations
    elif x1 > (88+(40*n)):
        canvas.move(x, -2, 0)
    # Move down the next 20 iterations
    elif move_rec_left.counter < 40:
        canvas.move(x, 0, 2)
        move_rec_left.counter += 1

    # else:
        # Reset the counter and move back to the original position
        # move_circle.counter = 0
        # canvas.move(circle, 2, -2)

   # move_rec_left.counter += 1
    if move_rec_left.counter < 40:
        root.after(40, move_rec_left, x, n)


def swap(x, indx, y, n):
    canvas.itemconfig(x, fill='red')
    canvas.itemconfig(y, fill='red')
    thread1 = threading.Thread(target=move_rec_right(y, indx))
    thread2 = threading.Thread(target=move_rec_left(x, n))

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

rec = canvas.create_rectangle(
    328.0, 289.0, 368.0, 329.0, fill='blue')  # Create a blue rectangle

# Set an initial counter value for the move_circle function
move_rec_left.counter = 0
move_rec_right.counter = 0


# Call the move_circle function to start the animation
# move_rec_right(a, 4)
swap(d, 4, b, 2)

root.mainloop()
