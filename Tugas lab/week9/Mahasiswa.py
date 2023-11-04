class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"

mahasiswa1 = Mahasiswa("John Doe", "12345678", "Teknik Informatika", 3.8)
mahasiswa1.tampilkan_info()
print("Predikat:", mahasiswa1.hitung_predikat())

mahasiswa2 = Mahasiswa("Jane Smith", "87654321", "Manajemen", 2.3)
mahasiswa2.tampilkan_info()
print("Predikat:", mahasiswa2.hitung_predikat())
