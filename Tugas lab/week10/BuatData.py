import os
import re

"""
function
"""
def garis(x = 50):
    return (f"+{'='*x}+")
def stringinbox(kata):
    return (f"|{kata.center(50)}|")
def clear():
    os.system("cls")

"""
INTERFACE
"""

while True:
    opsi = (f"""
{garis().center(50)}
{stringinbox("PILIH OPSI")}
|{("-"*50).center(50)}|
{stringinbox("1. Detail Anda")}
{stringinbox("2. Ubah Nama")}
{stringinbox("3. Jumlah Data Pada Files")}
{stringinbox("4. Save Data Pada Files")}
{stringinbox("5. Buat Data Baru")}
{stringinbox("6. keluar")}
{garis().center(50)}""")
    print(opsi)

    while True:
        try:
            inputan_penguna = int(input(f"|{'Masukan Opsi'.center(50)}|\n{garis().center(50)}\n\t\t\t: "))
            if inputan_penguna in [i for i in range(1,7)]:
                clear()
                break
            else: raise NameError
        except:
            clear()
            print(garis())
            print(f'|{"inputan anda tidak valid".center(50)}|')
            print(garis())
            print(opsi)


    """
    MATCHING INPUTAN PENGUNA
    """
    class datapenguna:
        def __init__ (self,nama,email,password):
            self.nama = nama 
            self.email = email
            self.__password = password

        def reset(self):
            self.__init__
        
        def getpassword(self):
            if self.__password:
                return self.__password
            else: raise TypeError
        def setpassword(self,passbarU):
            self.__password = passbarU
        def ubahnama(self,namabaru):
            if self.nama:
                self.nama = namabaru
            else:return TypeError

    match inputan_penguna:

        # Detail Anda
        case 1:
            clear()
            try:
                datapenguna1.getpassword()
                count = 0
                while True:
                    if input("Masukan Password untuk mengakses detail : ") == datapenguna1.getpassword():
                        break
                    else:
                        print(f"password salah")
                    
                while True:
                    print(f"""
                {garis().center(50)}
                {stringinbox("DATA ANDA")}
                |{("-"*50).center(50)}|
                {stringinbox(f"NAMA : {datapenguna1.nama}")}
                {stringinbox(f"Email : {datapenguna1.email}")}
                {stringinbox(f"PASSWORD : {datapenguna1.getpassword()}")}
                {garis().center(50)}""")
                            
                    if type(input()) == str:
                            clear()
                            break 
            except:
                print(f"{garis().center(50)}")
                print(stringinbox("Anda Belum Mengisi Data"))
                print(f"{garis().center(50)}")


        #UBAH NAMA
        case 2:
            try:
                if datapenguna1.nama == None:
                    raise{NameError}
                print(f"""
                {garis().center(50)}
                {stringinbox("UBAH NAMA")}
                {garis().center(50)}""")
                prom_input = f"""
                {garis().center(50)}
                {"Masukan Nama Baru".center(50)}
                {garis().center(50)}
                            : """
                datapenguna1.ubahnama(input(prom_input))
                clear()
                print(garis().center(50))
                print(stringinbox(f"berhasil mengubah nama menjadi {datapenguna1.nama}"))
                print(garis().center(50))

            except:
                print(f"{garis().center(50)}")
                print(stringinbox("Anda Belum Mengisi Data"))
                print(f"{garis().center(50)}")


        #menghitung jumlah data
        case 3:
            try:
                z = f"""
                    {garis().center(50)}
                    {stringinbox("Masukan Nama Files")}
                    {garis().center(50)}
                            :"""
                namafiless = input(z) + ".txt"
                dir_database = "C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/week10/DATABASE"
                os.chdir(dir_database)
                with open(namafiless,"r") as files:
                    count = len(files.readlines())
                    banyakdata = (count - 5)//6
                    print(garis().center(50))
                    print(stringinbox(f"Data dalam Files Sebanyak {banyakdata}"))
                    print(garis().center(50))
            except:
                print(f"{garis().center(50)}")
                print(stringinbox("File Tidak Ditemukan"))
                print(f"{garis().center(50)}")
 


        #save data pada files
        case 4:
            clear()
            dir_database = "C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/week10/DATABASE"
            os.chdir(dir_database)
            try:
                if datapenguna1.nama:
                    pass
                else:raise NameError
                z = f"""
                {garis().center(50)}
                {stringinbox("Masukan Nama Files")}
                {garis().center(50)}
                        :"""
                namafiles = input(z) + ".txt"
                print(f"{garis().center(50)}")
                if not os.path.exists(namafiles):
                    with open(namafiles,"w") as file1:
                        tabel = f"""
                        {garis().center(50)}
                        {stringinbox("DATA YANG TERSIMPAN")}
                        {garis().center(50)}
                        {stringinbox(f"Nama : {datapenguna1.nama}")}
                        |{("-"*50).center(50)}|
                        {stringinbox(f"Email : {datapenguna1.email}")}
                        |{("-"*50).center(50)}|
                        {stringinbox(f"Password: {datapenguna1.getpassword()}")}
                        {garis().center(50)}                
                        """
                        file1.write(tabel)
                        datapenguna1 = datapenguna(nama=None,email=None,password=None)
                else:
                    with open(namafiles,"a") as file1:
                        tabel = f"""{stringinbox(f"Nama : {datapenguna1.nama}")}
                        |{("-"*50).center(50)}|
                        {stringinbox(f"Email : {datapenguna1.email}")}
                        |{("-"*50).center(50)}|
                        {stringinbox(f"Password: {datapenguna1.getpassword()}")}
                        {garis().center(50)}
                        """
                        file1.write(tabel)
                        datapenguna1 = datapenguna(nama=None,email=None,password=None)
            except:
                print(f"{garis().center(50)}")
                print(stringinbox("Buatlah Data Baru Dahulu"))
                print(f"{garis().center(50)}")
            

        #buat data baru
        case 5:
            clear()
            print(f"{garis().center(50)}")
            nama = str(input(f"|{'Masukan Nama'.center(50)}|\n{'='*52}\n\t\t: "))

            while True:
                print(f"{garis().center(50)}")
                email = str(input(f"|{'Masukan Email'.center(50)}|\n{'='*52}\n\t\t: "))
                print(f"{garis().center(50)}")
                
                validasi = re.match(r"[a-z0-9]+@student\.unhas\.ac\.id",email)
                if validasi:
                    break
                else:
                    print(stringinbox("Email Yang Anda Masukan Salah"))
            while True:
                password = str(input(f"|{'Masukan Password'.center(50)}|\n{'='*52}\n\t\t: "))
                validasi = re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9]+$",password)
                panjang_password = re.match(r".{8,20}",password)
                if panjang_password:
                    if validasi:
                        break
                    else:
                        print(stringinbox(r"Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka"))

                else:print(r"Password harus memiliki Panjang 8 - 20 karakter")
                
            datapenguna1 = datapenguna(nama=nama,email=email,password=password)
            clear()
            print(f"{garis().center(50)}")
            print(stringinbox(" data disimpan sementara, sila save "))
            print(f"{garis().center(50)}")


        # keluar
        case 6:
            print(f"{garis().center(50)}")
            print(stringinbox("Sekian Terima Kasih"))
            print(f"{garis().center(50)}")
            exit()