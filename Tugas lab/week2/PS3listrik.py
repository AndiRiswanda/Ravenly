golong = ["R1","R2","R3","B2","B3","I3",'P1']

while True:
    gol   = (input("golongan = ").capitalize())
    if gol not in golong:
        print ("Golongan tidak valid")
    if gol in golong:
        break

daya  = int(input("daya = "  ))
pakai = int(input("pemakaian = "))

kwh = 0
valid = True

def kva (va):
  return 1000 * va

match gol:
    case "R1": 
        if daya == 900:
            kwh = 1352
        elif daya == 1300 or daya == 2200:
            kwh = 1444.70
        else:
            valid = False
    case "R2":
        if daya >= 3500 and daya <= 5.500:
            kwh = 1699.53
        else:
           valid = False           
    case "R3":
        if daya >= 6600:
            kwh = 1699.53
        else:
           valid = False          
    case "B2":
        if daya >= 6600 and daya <= kva(200):
            kwh = 1444.70
        else:
           valid = False
    case "B3":
        if daya > kva(200):
            kwh = 1114.74
        else:
           valid = False
    case "I3":
        if daya >= kva(200):
            kwh = 1114.74
        else:
          valid = False
    case "P1":
        if daya >= 6600 and daya <= kva(200):
            kwh = 1114.74
        else:
           valid = False
    case _:
       valid = False

hasil = kwh * pakai

if not valid:
    print ("data tidak valid")
else:
    #megubah ke string
    hasilSTR = str(hasil)
    #membelah decimal dan angka bulat menjadi dua variable
    noBulat, decimal = hasilSTR.split(".")
    #mengubah string nomor bular
    print ((f"Rp.{int(noBulat):,.0f}.{decimal}").replace(".", ","))