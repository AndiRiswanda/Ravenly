def space(a):
    print('\n' * a)
def permutasikata(kata):
    panjang = len(kata)
    hasil = []
    for i in range (panjang):
        kataterpotong = kata[i:] + kata[:i]
        hasil.append(kataterpotong)

    hasil = " | ".join(list(reversed(hasil)))
    
    return (f"{hasil}\n")


space(40)

print(permutasikata("Ayam"))
print(permutasikata("Rumah"))
print(permutasikata("Makan"))
print(permutasikata("Nasi"))
print(permutasikata("Sedap"))

space(20)