def angka_terbesar(*angka):
    angka = list(angka)
    try:
        for i in range (3):
            terbesar = angka[0]
            for nomor in angka:
                if nomor > terbesar:
                    terbesar = nomor
            angka.remove(terbesar)
    except :
        return("paramater kurang boss")
    return terbesar



print(angka_terbesar(37, 84, 29, 51, 12)) 

print(angka_terbesar(73, 93))

print(angka_terbesar(32,543,43,3432,532,234,324))

print(angka_terbesar(60, 85, 22, 56))