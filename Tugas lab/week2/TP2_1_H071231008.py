gen = ["1","2"]
while True:
    gender = input('''Pilih Gender anda: 
    1.Pria
    2.Wanita 
    Gender : ''')
    if gender not in gen:
        print ("input tidak valid")
    if gender in gen:
        break

tinggi = (int(input("Masukan Tinggi Badan Anda (cm) : "))/100)

berat = int(input("Masukan Berat Badan Anda (kg) : "))

BMI = berat / (tinggi) ** 2 

match gender :
    case "1":
        if BMI < 18:
            golongan = ("underweight")
        elif BMI >= 18 and BMI <= 23.9:
            golongan = ("normal")
        elif BMI >=24 and BMI <= 26.9:
            golongan = ("overweight")
        elif BMI >= 27:
            golongan = ("obese")
    case "2":
        if BMI < 17:
            golongan = ("underweight")
        elif BMI >= 17 and BMI <= 23.9:
            golongan = ("normal")
        elif BMI >=24 and BMI <= 27.9:
            golongan = ("overweight")
        elif BMI >= 28:
            golongan = ("obese")

print (f"anda tergolong {golongan} dengan BMI: {BMI:.2f}")