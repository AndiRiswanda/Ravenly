import os
os.system("cls")

'''
Funtion
'''
def Garis(x):
    print (f"{x}"*50)

def data_input(keys):
    while True:
        data[keys] = str(input(f"masukan {keys} anda : "))
        if data[keys] == "" :
            print (f"{keys} tidak boleh kosong")
        else: break

def opsi_user(x):
    match x:
        case "1" :
            print (f"""
Data Anda...
Nama    : {data['Nama']}
Umur    : {data['Umur']}
Alamat  : {data['Alamat']}
        """)
        case "2": data_input("Nama");print(f"\nUNama baru anda adalah : {data['Nama']}")
        case "3": data_input("Umur"); print(f"\nUmur baru anda adalah : {data['Umur']}")
        case "4": data_input("Alamat"); print(f"\nUNama baru anda adalah : {data['Alamat']}")
        case "5": return False
        case _ : return print ("Opsi Tidak Valid")


'''
DATA VARIABLE
'''
data = {}


'''
Interface
'''

Garis("-")
print ("""
Selamat datang :) 
Silakan Menginput data anda.
""")
Garis("-")
print("\n")

data_input("Nama")
data_input("Umur")
data_input("Alamat")

print("\n")

Garis("=")
print(f"Selamat Datang {data['Nama']}! Silahkan Pilih Opsi")
print("""
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
""")

Garis("=")
while True:
    if opsi_user(str(input("masukan opsi anda : "))) == False:
        print (f'Selamat Tingal {data["Nama"]}')
        break
    Garis("=")

