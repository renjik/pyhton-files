class students():
    def __init__(self,name, roll):
        self.name=name
        self.roll=roll
    def display(self):
        print( self.name)
        print (self.roll)
        print("age:",self.age,"marks:",self.marks)
    def setAge(self,age):
        self.age=age
    def setMarks (self,marks):
        self.marks=marks

a=students("ARJUN",10)
# print(a.name)
# print(a.roll)
a.setAge(15)
a.setMarks(50)
a.display()
