def FPB(x,y):
    x , y = y , x % y
    return x


def KPK(x, y):
    return x*y // FPB(x,y)


print(FPB(4,6))
print(FPB(5,15))


print(KPK(4,6))
print(KPK(5,15))
    
