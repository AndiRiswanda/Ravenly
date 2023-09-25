angkasatu = int(input("angka pertama: "))
angkadua = int(input("angka kedua: "))
operator = input("input operator: ")

match operator :

    case "-":
        hasil = angkasatu - angkadua
    case "+":
       hasil  = angkasatu + angkadua
    case "x" :
        hasil = angkasatu * angkadua
    case "/" :
        hasil = angkasatu // angkadua
    case _ :
        print ("operator anda tidak valid")


print(hasil)