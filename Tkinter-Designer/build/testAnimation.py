import tkinter as tk

def move_circle(dx, dy):
    canvas.move(circle, dx, dy)
    root.after(50, move_circle, dx, dy)  # Schedule the function to run again after 50 milliseconds

root = tk.Tk()
root.title("Simple Animation")

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

circle = canvas.create_oval(50, 50, 100, 100, fill='blue')  # Create a blue circle

# Call the move_circle function with a change in x and y coordinates
move_circle(2, 2)  # Change the circle's x and y coordinates by 2 pixels

root.mainloop()