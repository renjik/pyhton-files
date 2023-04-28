# import tkinter as tk
from tkinter import *

w = Tk()
w.title("To-Do List App") 
w.configure(background='black')
w.geometry('400x250')


# Create and pack the listbox
tasks = Listbox(w)
tasks.pack(side=BOTTOM,fill=X)
# tasks.pack(side=tk.BOTTOM, fill=tk.BOTH)

# scrollbar
scrollbar = Scrollbar(w)
scrollbar.pack(side=RIGHT, fill=Y)

# Set the scrollbar to the listbox
tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks.yview)

# Create and pack the entry and button for adding tasks
entry = Entry(w, width=70) 
entry.pack(padx=5, pady=5)

def addtask():
    # Add the task 
    task = entry.get()
    if task != "":
        tasks.insert(END, task)
        entry.delete(0, END)

def deletetask():
    # Delete the selected task 
    selection = tasks.curselection()
    if selection:
        tasks.delete(selection)

# button for adding tasks
add_button = Button(w, text="Add Task", command=addtask)
add_button.pack(side=BOTTOM)

# Create button for deleting tasks
delete_button = Button(w, text="Delete Task", command=deletetask)
delete_button.pack(side=BOTTOM)

w.mainloop() 