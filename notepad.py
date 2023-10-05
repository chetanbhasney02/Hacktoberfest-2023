import tkinter as tk
from tkinter import filedialog
import os

def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete('1.0', tk.END)

def open_file():
    global file
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Document", "*.txt")
        ]
    )

    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        textArea.delete('1.0', tk.END)
        f = open(file, 'r')
        textArea.insert("1.0", f.read())
        f.close()

def save_as_file():
    global file
    file = filedialog.asksaveasfilename(
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Document", "*.txt")
        ]
    )

    if file == '':
        file = None
    else:
        f = open(file, "w")
        f.write(textArea.get('1.0', tk.END))
        f.close()
        root.title(os.path.basename(file) + ' - Notepad')

def save_file():
    global file

    if file == None:
        save_as_file()
    else:
        f = open(file, "w")
        f.write(textArea.get('1.0', tk.END))
        f.close()

def copy():
    textArea.event_generate("<<Copy>>")

def cut():
    textArea.event_generate("<<Cut>>")

def paste():
    textArea.event_generate("<<Paste>>")

root = tk.Tk()
root.geometry("600x400")
root.title('Untitled.txt - Notepad')

file = None

textArea = tk.Text(root, width=600, height=400, fg="black", bg="white")
textArea.pack()

menuBar = tk.Menu(root)

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New File", command=new_file)
fileMenu.add_command(label="Open File", command=open_file)
fileMenu.add_command(label="Save File", command=save_file)
fileMenu.add_command(label="Save File As...", command=save_as_file)
fileMenu.add_command(label="Exit", command=root.quit)

menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = tk.Menu(menuBar, tearoff=0)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Paste", command=paste)

menuBar.add_cascade(label="Edit", menu=editMenu)

root.config(menu=menuBar)
root.mainloop()
