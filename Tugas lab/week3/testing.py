hargaBarang = int(input("Harga barang : "))
tunaiPembeli = int(input("Uang pembeli: "))
if tunaiPembeli < hargaBarang:
        print("Uang Tunai pembeli kurang!")
        exit()
u100,u50,u20,u10,u5,u2,u1 = [0]*7
baki = tunaiPembeli - hargaBarang
p = [baki-100000,baki-50000,baki-20000,baki-10000,baki-5000,baki-2000,baki-1000]

while baki > 0:
    if p[0] >= 0:
            u100 += 1
            baki -= 100000
    elif p[1] >= 0:
            u50 += 1
            baki -= 50000
    elif p[2] >= 0:
            u20 += 1
            baki -= 20000
    elif p[3] >= 0:
            u10 += 1
            baki -= 10000
    elif p[4] >= 0:
            u5 += 1
            baki -= 5000
    elif p[5] >= 0:
            u2 += 1
            baki -= 2000
    elif p[6] >= 0:
            u1 += 1
            baki -= 1000

print (f'''baki nya adalah
{u100} uang 100
{u50} uang 50
{u20} uang 20
{u10} uang 10
{u5} uang 5
{u2} uang 2
{u1} uang 1''')
