from tkinter import*

window = Tk()
window.title("LOGin form")
window.configure(bg="white")
window.geometry("650x400")


lb = Label(window,text="LOGIN FORM",bg="red",fg="white",font=10,width=27).place(x=10,y=20)
# lb.pack()

lb1 = Label(window,text="USERNAME",bg="green",fg="white",width=10).place(x=10,y=50)
lb2 = Label(window, text="PASSWORD",bg="green",fg="white",width=10).place(x=10,y=80)

en = Entry(window)
en.place(x=120,y=50)

en2 = Entry(window)
en2.place(x=120,y=80)

def display():
    l = Label(window,text="your name is "+en.get(),bg="white")
    l.place(x=10,y=180)
    l1 = Label(window, text="your password is"+en2.get(),bg="white")
    l1.place(x=10,y=200)


bn = Button(window,text="Login",bg="red",fg="white",command=display).place(x=140,y=120)


window.mainloop()