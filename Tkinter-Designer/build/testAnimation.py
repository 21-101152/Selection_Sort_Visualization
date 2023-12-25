import tkinter as tk

def on_entry_focus(event):
    # Change the border color when the entry gets focus
    entry_frame.config(borderwidth=2, relief="solid")

def on_entry_focusout(event):
    # Change the border color back when the entry loses focus
    entry_frame.config(borderwidth=0)

root = tk.Tk()
root.title("Entry with Stroke")

# Create a frame to act as the border
entry_frame = tk.Frame(root, borderwidth=0)
entry_frame.pack(padx=10, pady=10)

# Create the entry widget inside the frame
entry = tk.Entry(entry_frame, font=("Arial", 12))
entry.pack(fill="both", expand=True)

# Bind focus and focusout events to change the border color
entry.bind("<FocusIn>", on_entry_focus)
entry.bind("<FocusOut>", on_entry_focusout)

root.mainloop()
