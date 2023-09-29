def angka_terbesar(listAngka):
    terbesar = 0
    for nomor in listAngka:
        if nomor > terbesar:
            terbesar = nomor
    return terbesar



print(angka_terbesar([37, 84, 29, 51, 12]))

print(angka_terbesar([73, 93, 64, 4, 86]))

print(angka_terbesar([39, 76, 96, 71, 27]))

print(angka_terbesar([60, 85, 22, 56, 5]))

print(angka_terbesar([99, 49, 77, 89, 63]))

print(angka_terbesar([92, 15, 83, 78, 31]))

print(angka_terbesar([70, 2, 53, 8, 98]))

print(angka_terbesar([41, 14, 47, 9, 25]))

print(angka_terbesar([59, 30, 95, 3, 67]))

print(angka_terbesar([54, 91, 72, 24, 66]))
