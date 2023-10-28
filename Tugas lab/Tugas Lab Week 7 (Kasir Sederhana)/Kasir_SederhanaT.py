"""
MODULE IMPORTING

"""
import os
import random

"""
Konfirmasi Path Kerja

"""
os.system("cls")
os.chdir("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab")
pathkerja = os.path.join("Tugas Lab Week 7 (Kasir Sederhana)","KasirFiles")
pathInvoice = "C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/Tugas Lab Week 7 (Kasir Sederhana)/KasirFiles/Invoice"

"""
Costum Funtion

"""

def clearscreen():
    os.system("cls")


def garis(x,langkahawal =0, langkahakhir = 0):
    
    if langkahawal > 0:
        print("\n"*langkahawal)

    print("="*x)

    if langkahakhir > 0:
        print("\n"*langkahakhir)


def headline(kata,lebar = 0, panjang = 0):
    if panjang == 0:
        panjanggaris = len(kata*3)
    else:
        panjanggaris = panjang

    garis(panjanggaris,langkahakhir = lebar)
    print ((f"{kata}").center(50))
    garis(panjanggaris,langkahawal = lebar)


def InisialCapital(kata):
    kata = kata.title()
    kata = [x for x in kata if x.isupper()]

    if len(kata) < 3:
        for i in range(3-len(kata)):
            kata.append(kata[-1])
    kata = "".join(kata)

    if len(kata) > 3:
        kata = kata[0:3]
    return kata


def generatedkodenamafiles(NamaKasir):
    NamaFormated = (InisialCapital(NamaKasir)).upper()

    HasilTerminalEchoDate = os.popen('echo %date%').read()
    HasilTerminalEchotime = os.popen('echo %time%').read()

    waktu = HasilTerminalEchotime.split(":")
    waktujam = f"{int(waktu[0]):02}"
    waktumenit = f"{waktu[1]:02}"
    bulan, tanggal, tahun = HasilTerminalEchoDate.split("/")
    bulan = bulan.split()

    generatednum = f"{random.randint(100,999):03}"

    NamaFileFormated = "".join((NamaFormated, tahun[2:4], bulan[1], tanggal, waktujam ,waktumenit,generatednum,".txt"))

    return NamaFileFormated


def pencarianInvoice(namaInvoice):
    os.chdir(pathInvoice)
    try :
        with open((namaInvoice+".txt"), "r") as FileYangDitemukan:
            
            while True:
                clearscreen()
                print ("Oh Kami Menumakan Invoice Yang Anda Cari!")
                print (FileYangDitemukan.read())
                print("\n\n\x1B[1mEnter\x1B[0m" + " untuk lanjut")
                if type(input("...")) == str:
                    clearscreen()
                    break
                else:
                    continue
    except:
        while True:
            clearscreen()
            print("\n NOTIFIKASI : Maaf Kami Tidak Menemkan Invoice Yang Anda Cari :( \n")
            print("""
            ████████╗ █████╗ ██╗  ██╗         ██╗██╗   ██╗███╗   ███╗██████╗  █████╗         ██╗
            ╚══██╔══╝██╔══██╗██║ ██╔╝         ██║██║   ██║████╗ ████║██╔══██╗██╔══██╗    ██╗██╔╝
               ██║   ███████║█████╔╝          ██║██║   ██║██╔████╔██║██████╔╝███████║    ╚═╝██║ 
               ██║   ██╔══██║██╔═██╗     ██   ██║██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██║    ██╗██║ 
               ██║   ██║  ██║██║  ██╗    ╚█████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║    ╚═╝╚██╗
               ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝     ╚════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝        ╚═╝""")
            print("\n\n\x1B[1mEnter\x1B[0m" + " untuk lanjut")
            if type(input("...")) == str:
                        clearscreen()
                        break
            else:
                continue
        

def TabelTransaksiBarang(databarang,kode,metode):
    extensiTable = ""
    totalharga = 0

    Waktu_Transaksi     = (os.popen('echo %time%').read())[0:-4]
    Tanggal_Transaksi   = (os.popen('echo %date%').read())[0:-1]
    Kode_Transaksi      = (kode).replace(".txt", "")
    
    counter = 0
    for key, values in databarang.items():
        
        counter += 1
        nama = databarang[key][0].center(16)
        if len(databarang[key][0]) > 15:
            nama = nama[0:13] + "..'"
        harga = str(databarang[key][1]).ljust(25)
        jumlah = str(databarang[key][2]).center(10)
        total = str(databarang[key][3]).rjust(12)

        totalharga += databarang[key][3]
        extensiTable += f"\t| {nama} | {f'Rp{harga}'} | {jumlah} | {f'Rp{total}'} |\n"
        if counter != len(databarang):
            extensiTable += "\t================================================================================\n"
        else:
            extensiTable += "\t================================================================================"

    total = (f"\t|{'total'.center(44)} |{('Rp '+str(totalharga)).center(29)}|\n")
    total += ("\t================================================================================\n")

    
    if metode == "transaksi" or metode == "t":
        return f"""
==================================================================================================   
                                        Toko {dataKasir["nama"]}
================================================================================================== 
Nama Kasir          : {dataKasir['nama']}
Waktu Transaksi     : {(os.popen('echo %time%').read())[0:-4]}
Tanggal Transaksi   : {(os.popen('echo %date%').read())[0:-1]}
Kode Transaksi      : {(kode).replace(".txt", "")}
==================================================================================================

                                        DAFTAR PRODUK

        ================================================================================
        |      Nama        |         Harga               |   Jumlah   |       Total    |
        ================================================================================
{extensiTable}
{total}
==================================================================================================   
                               Terima Kasih Sudah Berbelanja :)
================================================================================================== 
"""
    
    elif metode == "riwayat" or metode == "r" :
        extensiriwayat  = "\n"
        extensiriwayat += (f"|{Waktu_Transaksi.center(43)}|{Kode_Transaksi.center(43)}|{str(totalharga).center(20)}|\n").rjust(119)
        extensiriwayat += ("==============================================================================================================").rjust(118)
        
        riwayat = f"        ==============================================================================================================\n"

        riwayat += ("|" + "RIWAYAT TRANSAKSI".center(108) + "|").rjust(118) + "\n"

        riwayat += f"        ==============================================================================================================\n"

        riwayat += (f'|{"Waktu".center(43)}|{"Kode Transaksi".center(43)}|{"Nominal Transaksi".center(20)}|').rjust(118)+"\n"

        riwayat += f"       ==============================================================================================================\n".rjust(119)

        riwayat += (f"{extensiriwayat[1:]}")

        try:
            os.chdir("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/Tugas Lab Week 7 (Kasir Sederhana)/KasirFiles")
            if not os.path.exists("trx_history.txt"):
                with open("trx_History.txt", "w") as fileriwayat:
                    fileriwayat.write(riwayat)
            else:
                with open("trx_History.txt", "a") as fileriwayat2:
                    fileriwayat2.write(extensiriwayat)
        except IOError as er:
            print("error")


def MAINopsiprosesor(opsi):
    match opsi:
        case 1:
            clearscreen()
            print("\n")
            headline("Pembelian Barang")
            while True:
                nama_produk = str(input("Masukan Nama Produk : "))
                while True:
                    harga_produk = (input("Masukan Harga Produk : "))
                    if not harga_produk.isdigit():
                        print ("Harus Menginputkan Harga Valid")
                        continue
                    else :
                        harga_produk = int(harga_produk)
                        break
                while True:
                    jumlah_produk = (input("Masukan Jumlah Produk : "))
                    if not jumlah_produk.isdigit():
                        print ("Harus Menginputkan jumlah Valid")
                        continue
                    else : 
                        jumlah_produk = int(jumlah_produk)
                        break
                
                dataproduk[nama_produk] = [nama_produk]
                (dataproduk[nama_produk]).append(harga_produk)
                (dataproduk[nama_produk]).append(jumlah_produk)
                (dataproduk[nama_produk]).append(jumlah_produk*harga_produk)
                print("\n")
                headline((f"Tambah Produk(Y/N)? {' '*10} "),panjang=50)
                while True:
                    breaker = (input(f"(Y/N){' '*10}: ")).lower()
                    if breaker == "n" or breaker == "y":
                        break
                    else: 
                        print("inputan tidak valid")
                        continue

                if breaker == "n":
                    clearscreen()
                    break
                else: continue
                    
            #Directories Invoice Dan Pengaksesan
            try:
                if os.getcwd() != ("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/Tugas Lab Week 7 (Kasir Sederhana)/KasirFiles"):
                    os.chdir("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/Tugas Lab Week 7 (Kasir Sederhana)/KasirFiles")
                    
                kodenama = generatedkodenamafiles(dataKasir["nama"])
                if os.path.exists("invoice") == False:
                    
                    os.mkdir("Invoice")
                    os.chdir("invoice")
                    
                    with open(kodenama, "w" ) as FileInvoice:
                        FileInvoice.write(TabelTransaksiBarang(dataproduk,kodenama,"t"))
                    TabelTransaksiBarang(dataproduk,kodenama,"riwayat")
                else:      
                    os.chdir("invoice")
                    with open(kodenama, "w" ) as FileInvoice:
                        FileInvoice.write(TabelTransaksiBarang(dataproduk,kodenama,"t"))
                    TabelTransaksiBarang(dataproduk,kodenama,"riwayat")
                    print(f"\nNOTIFIKASI : Transaksi Berhasi! Dengan Kode Special : {kodenama[0:-4]}\n")

            except IOError as er:
                print (f"\n NOTIFIKASI : Gagal Membuat Transaksi : {er}\n")

        case 2:
            clearscreen()
            headline(" Pencarian Barang ;) ",panjang=50)
            kodebarangtujuan = input("Ketik Kode Special Invoice Yang : ")
            clearscreen()
            pencarianInvoice(kodebarangtujuan)

        case 3:
            try:
                clearscreen()
                
                os.chdir("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/Tugas lab/Tugas Lab Week 7 (Kasir Sederhana)/KasirFiles")
                print("Tentu Boleh !, Ini Riwayat Transaksi anda.....")
                with open("trx_History.txt", "r") as file1:
                    print(file1.read())
                while True:
                    print("\n\n\x1B[1mEnter\x1B[0m" + " untuk lanjut")
                    if type(input("...")) == str:
                        clearscreen()
                        break
            except IOError:
                print ("Anda Belum Pernah Melakukan Transaksi")

        case 4:
            return False
        
        case _:
            print("input Invalid")


"""
VariablePenting

"""
dataKasir = {}



"""
Interface

"""
# memilih opsi
counter = 0
while True:
    # VariablePenting
    dataproduk = {}
    if counter < 1:
        
        headline("SELAMAT DATANG",lebar= 1,panjang = 50)
        dataKasir["nama"] = input(f"Masukan Nama Kasir?{' '*10} :  ")
        while dataKasir["nama"].isnumeric():
            print ("nama tidak valid")
            dataKasir["nama"] = input(f"Masukan Nama Kasir?{' '*10} :  ")


        clearscreen()

    headline(f"Selamat Datang {dataKasir['nama']}!",panjang=50)
        
    garis(50)

    print("""\nPiih Opsi : 
        
    1. Transaksi Baru
    2. Cari Transaksi
    3. Riwayat Transaksi
    4. Keluar
    """)
    if counter < 3:
        counter += 1
    garis(50)
    if MAINopsiprosesor(int(input("Pilih Opsi Diatas : "))) == False:
        clearscreen()
        print("\nTerimakasih, Selama Tinggal....\n")
        exit()




