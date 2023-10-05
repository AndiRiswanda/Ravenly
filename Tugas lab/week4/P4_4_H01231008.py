def catAndmouse2(catA,catB,mosC):
    cat1 = abs(catA - mosC)
    cat2 = abs(catB - mosC)

    if cat1 > cat2:
        print("Cat B menang")
    elif cat1 == cat2:
        print("Tikus menang")
    else: print("Cat A menang")

catAndmouse2(catA=16, catB=24, mosC=15)#A menang
catAndmouse2(catA=20, catB=10, mosC=15)#tikus menang
catAndmouse2(catA=1, catB=25, mosC=15)#b menang
