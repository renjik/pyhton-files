class Temp():
    def __init__(self,c):
        self.celsius=c

    def Fahrenheit(self):
        return self.celsius*1.8 + 32

a=Temp(30)
print(a.Fahrenheit())





# Celsius (°C) = (Fahrenheit - 32) / 1.8.