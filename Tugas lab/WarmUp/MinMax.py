def kecilbesar(listx):
    kecil = listx[0]
    besar = listx[0]

    for i in listx:
        if i < kecil:
            kecil = i
        if i >= besar:
            besar = i
    
    return (f"{kecil},{besar}")


print(kecilbesar([1 ,2, 3, 4, 5]))