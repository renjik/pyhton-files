# try 
# except



# try :
#     n=6
#     print(n)
#     x = 5
#     y= 1
#     z =x/y
#     print(z) 
   
# except ZeroDivisionError:
#     print('error happened')

# except NameError:
#     print('n is not defined')

# else:
#     print('nothing happened')

    
# print('hello')
# print(10+5)

try:
  f = open("demo1file.txt", 'x') 
  try:
    f.write("Lorum Ipsum\n")
    f.write('hello world')
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 