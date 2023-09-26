nomor = int(input("masukan nomor carian anda : "))
a = 0
b = 0

while nomor > 0:
    c = a + b
    print (c, end=" ")
    b,a = a,c
    if a + b == 0:
        b = 1
    nomor -= 1