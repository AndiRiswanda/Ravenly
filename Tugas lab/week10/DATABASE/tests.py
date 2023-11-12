import os

def clearscreen():
    os.system("cls")

class BasisDataMahasiswa:
    def __init__(self):
        self.mahasiswa = {}

    def tambah_mahasiswa(self, nim, nama):
        self.mahasiswa[nim] = nama

    def edit_mahasiswa(self, nim, nama_baru):
        if nim in self.mahasiswa:
            self.mahasiswa[nim] = nama_baru
            print(f"Mahasiswa dengan NIM {nim} telah diperbarui.")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def hapus_mahasiswa(self, nim):
        if nim in self.mahasiswa:
            del self.mahasiswa[nim]
            print(f"Mahasiswa dengan NIM {nim} telah dihapus.")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def tampilkan_mahasiswa(self):
        print("Daftar Mahasiswa:")
        for nim, nama in self.mahasiswa.items():
            print(f"NIM: {nim}, Nama: {nama}")

while True:
    print(f"+{('='*48).center(50)}+")
    print(f"|{'DATABASE MAHASISWA'.center(50)}|")
    print(f"+{('='*48).center(50)}+")
    print(f"|{'PILIH OPSI'.center(50)}|")
    print(f"+{('='*48).center(50)}+")

    print(f"+{('='*48).center(50)}+")
    print("""    1.\t\t   Tambah Data\n    2.\t\t   Edit Data\n    3.\t\t   Delete Data    \n    4.\t\t   Tampilkan info mahasiswa\n    5.\t\t   keluar""")
    print(f"+{('='*48).center(50)}+")
    inputpenguna = input("masukan opsi : ")


    match inputpenguna:

        case "1":
            #tambah data
            clearscreen()
            data1 = BasisDataMahasiswa()
            print(f"+{('='*48).center(50)}+")
            print(f"|{'MENAMBAH DATA'.center(50)}|")
            print(f"+{('='*48).center(50)}+")

            nim = input("Masukan Nim Kamu: ")
            nama = input("Masukan Nama Kamu: ")
            data1.tambah_mahasiswa(nim,nama)
            data1.tampilkan_mahasiswa()
            
        case "2":
            clearscreen()
            print(f"+{('='*48).center(50)}+")
            print(f"|{'MENGEDIT DATA'.center(50)}|")
            print(f"+{('='*48).center(50)}+")
            nimbaru = input("Masukan Nim Kamu: ")
            namabaru = input("Masukan Nama Kamu: ")
            clearscreen()

        case "3":
            clearscreen()
            print(f"+{('='*48).center(50)}+")
            print(f"|{'MENGHAPUS MAHASISWA'.center(50)}|")
            print(f"+{('='*48).center(50)}+")
            d = input("masukan nim mahasiswa yang ingin dihapus: ")
            clearscreen()
            data1.hapus_mahasiswa(d)
        case "4":
            clearscreen()
            print(f"+{('='*48).center(50)}+")
            print(f"|{'DATA MAHASISWA'.center(50)}|")
            print(f"+{('='*48).center(50)}+")
            data1.tampilkan_mahasiswa()
        case "5":
            exit()
    
