print("Length of the Triangle sides")
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x==y==z:
    print("Its Equalateral")
elif x==y or y==z or x==z:
    print("isosceles")
else:
    print("scalene")