# def input_user(inputt):
#     promt = int(input(inputt))
#     return promt

# def luaspermukaan(p,l,t):
#     return 2*((p*l)+(p*t)+(l*t))

# def volumebalok(p,l,t):
#     return p*l*t

# def cetak(output):
#     print(output)


# p = input_user("masukan nilai panjang ")
# l = input_user("masukan nilai lebar ")
# t = input_user("masukan nilai tinggi ")

# cetak(f"volume : {volumebalok(p,l,t)}\nluaspermukaan:{luaspermukaan(p,l,t)}")


name = ["andi","ciwan","riswanda"]
gaji = [1000,1082308,33433,11323]

def ratarata(gaji= "list"):
    return gaji/len(gaji)

def data_karyawan(nama):
    for a in nama:
        return (f"nama karyawan :{a}\n")
def data_karyawan2(gaji):
    for a in gaji:
        return (f"gaji :{a}\n")


print (f"nama karyawan {data_karyawan(name)}\n {data_karyawan2(gaji)}")
