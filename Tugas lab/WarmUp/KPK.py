def KPK(x, y):

    greater = max(x,y)
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def FPB(x,y):
    greater = max(x,y)
    while True:
        if x % greater == 0 and y % greater == 0:
            break
        greater -= 1
    return greater
    



print(FPB(4,6))
print(FPB(5,15))


print(KPK(4,6))
print(KPK(5,15))
    
