from tkinter import *

s = Tk()
s.geometry("600x400")
s.resizable(False,False)
s.title('sample tkinter')
s.configure(background='black' )

lb = Label(s,text='username').place(x=20,y=70)
# lb.pack()

en = Entry(s)
en.pack()



lb1 = Label(s,text="password").place(x=20,y=100)



s.mainloop()