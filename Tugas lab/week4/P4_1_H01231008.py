def permutasikata(kata):
    if type(kata) == str:
        if kata.isnumeric():
            print("input masih berupa Angka")
            exit()
    try :
        panjang = len(kata)
        hasil = ""
        for i in range (panjang):
            kataterpotong = kata[-1:] + kata[:-1]
            hasil += kataterpotong + " | "
            kata = kataterpotong    
        return (f"{hasil}\n")
    except TypeError:
        return(f"Input {kata} tidak valid \nHarus Menginput String!\n")


print(permutasikata("Ayam"))
print(permutasikata("Rumah"))
print(permutasikata(3398))
print(permutasikata("Makan"))
print(permutasikata("Nasi"))
print(permutasikata(input()))

