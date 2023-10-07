def hitunghitung(n,m,x,y):
    ganda = n - x
    essay = 2*(m - y)
    maximum = ((20 + (15*2))/2)


    if (ganda + essay) > maximum:
        return "LOLOS"
    else: return "TIDAK LOLOS"


n,m,x,y = map(int, input().split())
print(hitunghitung(n,m,x,y))