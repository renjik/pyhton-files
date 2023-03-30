def poem(a,b,c):

    # print("the song is :",songs)
    songs = open("poem1.txt","w")
    songs.write(a+"\n")
    songs.write(b+"\n")
    songs.write(c+"\n")
    songs = open("poem1.txt","r")  
    print(songs.read()) 
    songs.close() 

poem(a=input("enter:"),b=input("enter:"),c=input("enter:"))

    # fun = open("poem.txt","w")

    # fun.write(" sing the poem\n sing sing sing a song")
    # fun = open("poem.txt","r")
    # print(fun.read())

    # fun.close()


# for i in range(3):
#     x = input('enter:')


