from tkinter import*



obj= Tk()
obj.title("todo")
obj.geometry("500x400")
obj.configure(background="white")
obj.resizable(False,False)

# en = Entry(obj,width=30,)
# en.pack(padx=50,pady=50)

resizedHeight = Entry(bg="white", fg="black")
resizedHeight.place(x=50, y=50, width=250, height=80)

b = Button(text="ADD",height=4,bg="black",fg="white").place(x=340,y=50)
b1 = Button(text="DEL",height=4,bg="black",fg="white").place(x=400,y=50)
  
# lb = Label(obj,text="",bg="black",fg="white")
# lb.pack()

box = Listbox(obj,width=50).place(x=50,y=150)

# h = Listbox(obj,width=50)
# h.place(x=50,y=150)

# box.insert(1,'python')

# h.pack()
# # lb.pack()


obj.mainloop()