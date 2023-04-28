class family:
    def members(self,names,age):
        self.names=names
        self.age=age
        print(self.names,self.age)
class parent(family):
    def child(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
    
obj = parent()
obj.members('aa',23)
obj.child("bb",21)

class college:
    def department(self,clases,divion):
        self.clases=clases
        self.divion=divion
        print(self.clases,self.divion)

class schools(college):
    def names(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

obj=schools()
obj.department("bcom","d")
obj.department("bsc cs","c")
obj.names("rj",21)


class names:
    def name(self,name,place):
        self.name=name
        self.place=place
        print(self.name,self.place)

class areas(names):
    def spot(self,area,street):
        self.area=area
        self.street=street
        print(self.area,self.street)

obj = areas()
obj.name("vishnu","manjeri")
obj.spot("vtk","xyz")