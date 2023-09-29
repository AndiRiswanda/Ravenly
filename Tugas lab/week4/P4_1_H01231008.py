"""
BELUM SEMPURNA

"""
kata = "ayam"
kata = list(kata)

for i in range (1,len(list(kata))):
    potongan = kata[i:len(list(kata))]

    kataTerpotong = "".join(kata).strip("".join(potongan))
    print (potongan,kataTerpotong, sep = "")
