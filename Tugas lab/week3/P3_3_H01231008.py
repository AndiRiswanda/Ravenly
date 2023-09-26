def conversijam(derajatD):
    derajatD *= 240
    jam = int(derajatD // 3600)+6
    if jam >= 24:
        jam %= 24
    menit = int(derajatD % 3600 // 60)
    derajatD = int(derajatD % 3600 % 60)
    return  (f"{jam:02}:{menit:02}:{derajatD:02}")
while True:
    try:
        derajat = float(input("Masukan Posisi Matahari (Derajat) : "))
    except ValueError:
        print ("Invalid Input")
        exit()
    if 0 <= derajat <=360:
        break

if derajat >= 0 and derajat <= 90: 
    Waktu = "Pagi"
elif derajat > 90 and derajat <= 180:
    Waktu = "Siang"
elif derajat > 180 and derajat <= 270:
    Waktu = "Sore"
else:Waktu = "Malam"

print (f"Selamat {Waktu}\n{conversijam (derajat)}")




