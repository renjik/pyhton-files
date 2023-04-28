from tkinter import*

x = Tk()
x.title("To-Do")
x.configure(background="white")
x.geometry("400x250")

task = Listbox(x)
task.pack(side=BOTTOM,fill=Y)

task1 = Scrollbar(x)
task1.pack(side=TOP,fill=X)

task.config(yscrollcommand=Scrollbar.set)
task1.config(command=task.yview)

entry = Entry(x,width=50)
entry.pack(padx=5,pady=5)

def addtask():
    add = entry.get()
    if add != "":
        task.insert(END, task)
        entry.delete(0, END)

def deletetask():
    # Delete the selected task 
    selection = task.curselection()
    if selection:
        task.delete(selection)

add_button = Button(x, text="Add Task", command=addtask)
add_button.pack(side=BOTTOM)

delete_button = Button(x, text="Delete Task", command=deletetask)
delete_button.pack(side=BOTTOM)

x.mainloop()