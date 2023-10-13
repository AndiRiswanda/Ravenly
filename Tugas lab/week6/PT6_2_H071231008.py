array1 = input("Input array ke-1 : ")
array2 = input("Input array ke-2 : ")

array1 = set(map(int,array1.split()))
array2 = set(map(int,array2.split()))

hasil = array1.intersection(array2)
if len(hasil) != 0:
    print(f"terdapat {len(hasil)} buah duplikat yaitu {tuple(hasil)} ")
else : print ("Tidak Ada Duplikat Ditemukan")