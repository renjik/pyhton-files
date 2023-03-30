import json

# json object to python object---load() 
x = '{"name":"nimisha","age":21}' 
print(type(x))
y=json.loads(x)
print(type(y))
print(y)

# python ob to json ob---dumps

m = [1,2,5]
n=json.dumps(m)
print(n)
print(type(n))

x=(1,2,3)
y=json.dumps(x)
print(type(y))
print(y)

int = 5
z=json.dumps(int)
print(type(z))
print(z)

stre = "renjik"
nam=json.dumps(stre)
print(type(nam))
print(nam)

a = 32.5
b = json.dumps(a)
print(type(b))
print(b)

a = 30
b = 20
if a>b:
    print(json.dumps(True))

a = 10
b = 15
if a<b:   
    print(json.dumps(False))

