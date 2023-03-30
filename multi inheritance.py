class school:
    def hello(self):
        print('hai')

class student(school):
    def display(self):
        print('hello')

class teacher(student):
    pass

obj = teacher()
obj.hello()
obj.display()

class family:
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
obj.show()
obj.father_name("Ramesh")
obj.child_name("Vishnu",15)

class company:
    def Company_name(self):
        print("Scave")

class Properties(company):
    def works(self,designs,posters,branding,webdevelop,marketing):
             self.designs=designs
             self.posters=posters
             self.branding=branding
             self.webdevelop=webdevelop
             self.marketing=marketing
             print("<<Prizing>>","\n","designing:",self.designs,"\n","posters  :",self.posters,"\n","Branding :",self.branding,"\n","web      :",self.webdevelop,"\n","Marketing:",self.marketing)

class workers(Properties,company):
             def worker(self,name,place):
                    self.name=name
                    self.place=place
                    print(" Name:",self.name,"\n","Place:",self.place)

obj = workers()
obj.Company_name()
obj.works(300,250,400,5000,2000)
obj.worker("Vishnu","majri")
obj.worker("sujin","mlpm")

            
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             