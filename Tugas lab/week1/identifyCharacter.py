# input user
# diasumsikan hanya satu huruf atau satu angka positif
karakter = input("masukan karakter : ")

# membuat list
uppercase   = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
               "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lowercase   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

number      = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# cek kapital
kapital = karakter in uppercase
# cek huruf kecil
lowcase = karakter in lowercase
# cek nomor
nomor = karakter in number

print (f'''Kapital = {kapital} 
Huruf kecil = {lowcase},
Nomor = {nomor}''')