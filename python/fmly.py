
class family:
    place='kochi'
    age = 78
    def show(self):
        print("Family")

class father(family):
    def father_name(self,name):
        self.name=name
        print("Father_name:",self.name)

class child(father,family):
    def child_name(self,name,age):
        self.name=name
        self.age=age
        print(" Child_name:",self.name,"\n","Child_age :",self.age)

obj=child()
# obj.show()
# obj.father_name("Ramesh")
# obj.child_name("Vishnu",15)