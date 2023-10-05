def angka_terbesar(*angka):
    terbesar = angka[0]
    for nomor in angka:
        if nomor > terbesar:
            terbesar = nomor
    return terbesar

print(angka_terbesar(37, 84, 29, 51, 12))

print(angka_terbesar(73, 93))

print(angka_terbesar(39, 76, 96, 27))

print(angka_terbesar(60, 85, 22, 56))

print(angka_terbesar(99, 49, 63))

print(angka_terbesar(92, 15, 83, 78, 31))

print(angka_terbesar(70, 2,))

print(angka_terbesar(41))

print(angka_terbesar(59, 30, 95, 3, 67))

print(angka_terbesar(54, 91, 72))
