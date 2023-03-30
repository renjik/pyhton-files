import calculater

print("1.add","2.sub","3.multi","4.mode","5.per")
choice=int(input("Enter your choice:"))
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if choice==1:
    calculater.add(a,b)

if choice==2:
    calculater.sub(a,b)

if choice==3:
    calculater.multi(a,b)

if choice==4:
    calculater.mode(a,b)

if choice==5:
    calculater.per(a,b)

    