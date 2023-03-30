def story():
    stories = open("story.txt","w")
    count = 0
    a = "There are more lions in the jungle"
    x = a.lower()
    b = "There are many trees"
    y = b.lower()
    c = "Trees folds thier leefs"
    z = c.lower()

    if x[0]!="t":
        count+=1
        pass
    if y[0]!="t":
        count+=1
        pass
    if z[0]!="t":
        count+=1
        
    stories = open("story.txt","r")
    print(count)

    stories.close()
story()

    
    
    