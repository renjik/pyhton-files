from tkinter import*

window = Tk()
window.title("project")
window.configure(bg="white")
window.geometry("650x450")
lb = Label(window,text="STUDENT MARK LIST",bg="white",fg="black",font=30,width=20,)
lb.place(x=10,y=20)

lb1 = Label(window,text="NAME",fg="black",bg="white")
lb1.place(x=28,y=60)

en1 = Entry(window)
en1.place(x=80,y=60)

lb2 = Label(window,text="Enrol no",fg="black",bg="white")
lb2.place(x=260,y=60)

en2 = Entry(window)
en2.place(x=330,y=60)

lb3 = Label(window,text="SUBJECTS",bg="black",fg="white",width=20)
lb3.place(x=30,y=110)
lb4= Label(window,text="MARKS",bg="black",fg="white",width=20)
lb4.place(x=194,y=110)
lb5 = Label(window,text="GRADE",bg="black",fg="white",width=20)
lb5.place(x=358,y=110)
lb6 = Label(window,text="English",bg="grey",fg="black",width=20)
lb6.place(x=30,y=131)
lb4= Label(window,text="",bg="grey",fg="white",width=20)
lb4.place(x=194,y=131)
lb5 = Label(window,text="",bg="grey",fg="white",width=20)
lb5.place(x=358,y=131)




window.mainloop()