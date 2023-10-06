"""
Python ToDo GUI

Created a ToDo list in python using tkinter

"""


import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def mark_as_complete():
    try:
        selected_index = listbox.curselection()
        listbox.itemconfig(selected_index, {'bg':'#90EE90'})
    except:
        messagebox.showwarning("Warning", "Select a task to mark as complete!")

def delete_task():
    try:
        selected_index = listbox.curselection()
        listbox.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Create main window
root = tk.Tk()
root.title("To-Do List Application")

# Create widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

entry = tk.Entry(frame, font=('Arial', 14), width=30)
entry.grid(row=0, column=0, padx=(0, 10))


# Create buttons

frame_btns = tk.Frame(root, padx=10, pady=10)
frame_btns.pack(pady=10)

add_button = tk.Button(frame_btns, text="Add Task", command=add_task, font=('Arial', 12))
add_button.pack(side=tk.LEFT, padx=10)

mark_button = tk.Button(frame_btns, text="Mark as Complete", command=mark_as_complete, font=('Arial', 12))
mark_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(frame_btns, text="Delete Task", command=delete_task, font=('Arial', 12))
delete_button.pack(side=tk.LEFT, padx=10)


# Create listbox
frame2 = tk.Frame(root, padx=10, pady=10)
frame2.pack(pady=10)

listbox = tk.Listbox(frame2, selectbackground='#90EE90', font=('Arial', 12), width=40, height=10)
listbox.grid(row=0, column=1)

# Start main event loop
root.mainloop()


# This code is contributed by Shrimad Bhagwat 
# https://github.com/Shrimad-Bhagwat