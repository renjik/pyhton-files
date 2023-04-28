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

































