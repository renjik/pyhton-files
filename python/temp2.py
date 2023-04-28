class Temp():
    def __init__(self,f):
        self.Fahrenheit=f

    def celsius(self):
        return self.Fahrenheit-32/ 1.8

a=Temp(30)
print(a.celsius())