from tkinter import*

obj = Tk()
obj.geometry("400x200")
obj.resizable(False,False)
obj.configure(background="dark blue")
# lb = Label(obj,text="USERNAME",bg='blue',fg='white').place(x=80,y=40)
# en=Entry(obj).place(x=170,y=40)
# # en.pack()
# lb1 = Label(obj,text="PASSWORD",bg="blue",fg="white").place(x=80,y=70)
# en1 = Entry(obj).place(x=170,y=70)

# lb2 = Label(obj,text="ADDRESS",padx=7,bg='blue',fg='white').place(x=80,y=100)
# en2 = Entry(obj).place(x=170,y=100)

def add():
    lb = Label(obj,text="USERNAME",bg='blue',fg='white').place(x=80,y=40)
    en=Entry(obj).place(x=170,y=40)
# en.pack()
    lb1 = Label(obj,text="PASSWORD",bg="blue",fg="white").place(x=80,y=70)
    en1 = Entry(obj).place(x=170,y=70)

    lb2 = Label(obj,text="ADDRESS",padx=7,bg='blue',fg='white').place(x=80,y=100)
    en2 = Entry(obj).place(x=170,y=100)


b = Button(text="register",bg="blue",fg="white",command=add).place(x=150,y=140)
# b.pack()



obj.mainloop()