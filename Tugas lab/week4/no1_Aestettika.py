import os


def header(string):
    print ("\033[01m")
    print ("\033[32m")
    print ("\n"+ ("="*len(string)))
    print (string)
    print (("="*len(string) )+"\n")
    print ("\033[0m")

def clearscreen():
    os.system("cls")
    
def permutasikata(kata):
    try :
        panjang = len(kata)
        hasil = []
        for i in range (panjang):
            kataterpotong = kata[i:] + kata[:i]
            hasil.append(kataterpotong)

        hasil = " | ".join(list(reversed(hasil)))
    
        return (f"{hasil}\n")
    except TypeError:
        return(f"Input {kata} tidak valid \nHarus Menginput String!\n")


clearscreen()
header("Hasilnya Adalah")

print(permutasikata("Ayam"))
print(permutasikata("Rumah"))
print(permutasikata(3398))
print(permutasikata("Makan"))
print(permutasikata("Nasi"))
print(permutasikata(123))

header("Terima Kasih Sudah Mengunakan Program ini")



