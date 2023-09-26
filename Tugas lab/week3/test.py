harga = 100000
tunai = 322000
if tunai < harga:
    print("Uang Tunai pembeli kurang!")
    exit()

baki = tunai - harga
p = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
o = [0] * 7

print ("baki tunai adalah")
for i in range(len(p)):
    while baki >= p[i]:
        o[i] += 1
        baki -= p[i]

print (f'''baki nya adalah
{o[0]} uang 100
{o[1]} uang 50
{o[2]} uang 20
{o[3]} uang 10
{o[4]} uang 5
{o[5]} uang 2
{o[6]} uang 1''')
