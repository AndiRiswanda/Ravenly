harga = int(input("Harga barang : "))
tunai = int(input("Uang pembeli: "))
if tunai < harga:
        print("Uang Tunai pembeli kurang!")
        exit()

baki = tunai - harga
p = [100000,50000,20000,10000,5000,2000,1000]
o = [u100,u50,u20,u10,u5,u2,u1] = [0]*7

print ("baki tunai adalah")
while baki > 0:
    for i in p:
        q = p.index(i)
        if i - baki <= 0:
            o[q] += 1
            baki -= i
            print (f"{o[q]} uang {p[q]}")
        else:
            print (f"{o[q]} uang {p[q]}")