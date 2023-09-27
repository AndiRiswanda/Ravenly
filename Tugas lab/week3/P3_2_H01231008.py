harga = int(input("Harga barang : "))
tunai = int(input("Uang pembeli: ")) - harga

p = [100000,50000,20000,10000,5000,2000,1000]
o = [0]*7

for i in range (len(p)):
    while tunai - p[i] >= 0:
        o[i] += 1
        tunai -= p[i]
    print (f"{o[i]} uang {p[i]}")