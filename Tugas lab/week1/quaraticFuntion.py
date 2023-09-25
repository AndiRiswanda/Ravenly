#meminta user menginput nilai a
a = int(input("nilai a : "))
while a == 0:           #mengulang perintah input sehingga tidak sama dengan 0
    print ("tidak boleh sama dengan nol")
    a = int(input("nilai a : "))
b = int(input("nilai b : "))
c = int(input("nilai c : "))

# perhitugan x1                          
x1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
# perhitungan x2
x2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)

# print dengan format 2 angka dibelakang koma (:.2f)
print (f'''X1 : {x1:.2f}
X2 : {x2:.2f}''')