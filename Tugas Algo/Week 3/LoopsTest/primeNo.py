number = [1,2,3,4,5,6,7,8,9,10]

for x in number:
    for c in range(2,x):
        if (x%c == 0) :
            print ("bukan prime")
        elif x//c == x:
            print (x)