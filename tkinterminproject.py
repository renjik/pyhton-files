from tkinter import*

window = Tk()
window.title("project")
window.configure(bg="white")
window.geometry("650x450")
student_mark_list = Label(window,text="STUDENT MARK LIST",bg="black",fg="white",font=('italic',15),width=20,)
student_mark_list.place(x=10,y=20)

name_lb = Label(window,text="NAME",fg="black",bg="white")
name_lb.place(x=28,y=60)



enrol_no = Label(window,text="Enrol no",fg="black",bg="white")
enrol_no.place(x=260,y=60)


subject_name = Label(window,text="SUBJECTS",bg="black",fg="white",width=20)
subject_name.place(x=30,y=110)
mark_name= Label(window,text="MARKS",bg="black",fg="white",width=19)
mark_name.place(x=175,y=110)
grade_name = Label(window,text="GRADE",bg="black",fg="white",width=20)
grade_name.place(x=311,y=110)
english_lb = Label(window,text="English",bg="grey",fg="black",width=20)
english_lb.place(x=30,y=131)
hindi_lb = Label(window,text="Hindi",bg="black",fg='white',width=20)
hindi_lb.place(x=30,y=152)
science_lb= Label(window,text="Science",bg="grey",fg="black",width=20)
science_lb.place(x=30,y=173)
maths_lb = Label(window,text="Maths",bg="black",fg="white",width=20)
maths_lb.place(x=30,y=194)



name_entry = Entry(window)
name_entry.place(x=80,y=60)

enrol_no_entry = Entry(window)
enrol_no_entry.place(x=330,y=60)

english_entry1=Entry(window,text="",bg="grey",fg="white",width=23)#mark
english_entry1.place(x=175,y=132,)
english_entry2 = Entry(window,text="",bg="grey",fg="white",width=24)#grade
english_entry2.place(x=310,y=132)

hindi_entry1 = Entry(window,bg="black",fg="white",width=23)#mark
hindi_entry1.place(x=175,y=153)
hindi_entry2 = Entry(window,bg="black",fg="white",width=24)#grade
hindi_entry2.place(x=310,y=153)

science_entry1 = Entry(window,bg="grey",fg="black",width=23)#mark
science_entry1.place(x=175,y=175)
science_entry2 = Entry(window,bg="grey",fg="black",width=24)#grade
science_entry2.place(x=310,y=175)

maths_entry1 = Entry(window,bg="black",fg="white",width=23)#mark
maths_entry1.place(x=175,y=196)
maths_entry2 = Entry(window,bg="black",fg="white",width=24)#grade
maths_entry2.place(x=310,y=196)



def display():
    name_label = Label(window,text="Student Name :"+name_entry.get(),fg="red",bg="white")
    name_label.place(x=30,y=300)

    enrol_no_label = Label(window,text="Enrol no :"+enrol_no_entry.get(),fg="red",bg="white")
    enrol_no_label.place(x=30,y=320)

    grade_card_lb = Label(window,text="GRADE CARD",bg="white",fg="black",font=("bold",10))
    grade_card_lb.place(x=30,y=340)

    out_of_400 = Label(window,text="Out of 400",bg="white",fg="black")
    out_of_400.place(x=30,y=360)


    subject_name_lb = Label(window,text="SUBJECTS",bg="blue",fg="white",width=20)
    subject_name_lb.place(x=30,y=400)
    # subject_name_lb.pack()
    mark_name_lb= Label(window,text="MARKS",bg="blue",fg="white",width=20)
    mark_name_lb.place(x=175,y=400)

    grade_name_lb = Label(window,text="GRADE",bg="blue",fg="white",width=20)
    grade_name_lb.place(x=311,y=400)


    english_lb1 = Label(window,text="English",bg="blue",fg="white",width=20)
    english_lb1.place(x=30,y=430)

    hindi_lb1 = Label(window,text="Hindi",bg="blue",fg='white',width=20)
    hindi_lb1.place(x=30,y=460)

    science_lb1= Label(window,text="Science",bg="blue",fg="white",width=20)
    science_lb1.place(x=30,y=490)

    maths_lb1 = Label(window,text="Maths",bg="blue",fg="white",width=20)
    maths_lb1.place(x=30,y=520)








b1 = Button(window,text="SUBMIT",bg="blue",fg="white",width=10,activebackground="green",command=display)
b1.place(x=380,y=230)


window.mainloop()