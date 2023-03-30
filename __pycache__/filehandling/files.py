x = open('./sample/sample.txt','w')


x.write('my name is renji')


x = open('./sample/sample.txt','r')
print(x.read())

x.close()