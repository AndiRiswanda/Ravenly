N = int(input("Fibonaci : "))
a,b = 0, 1
for _ in range(N):
    print (a, end=" ")
    b,a = a, a+b