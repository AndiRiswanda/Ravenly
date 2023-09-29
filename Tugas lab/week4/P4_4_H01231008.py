def catAndmouse1(catA,catB,mosC):
    if mosC > catA: 
        cat1 = -(catA - mosC)
    else:
        cat1 = (catA-mosC)
    if mosC > catB: 
        cat2 = -(catB - mosC)
    else:
        cat2 = (catB-mosC)

    if cat1 > cat2:
        print("Cat B menang")
    elif cat1 == cat2:
        print("Tikus menang")
    else: print("Cat A menang")

def catAndmouse2(catA,catB,mosC):
    cat1 = abs(catA - mosC)
    cat2 = abs(catB - mosC)

    if cat1 > cat2:
        print("Cat B menang")
    elif cat1 == cat2:
        print("Tikus menang")
    else: print("Cat A menang")

catAndmouse1(catA=16, catB=24, mosC=15)#A menang
catAndmouse1(catA=20, catB=10, mosC=15)#tikus menang
catAndmouse1(catA=1, catB=25, mosC=15)#b menang

print("\n")

catAndmouse2(catA=16, catB=24, mosC=15)#A menang
catAndmouse2(catA=20, catB=10, mosC=15)#tikus menang
catAndmouse2(catA=1, catB=25, mosC=15)#b menang
