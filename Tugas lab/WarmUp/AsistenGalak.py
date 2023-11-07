"""
Pada pertemuan pertama di hadiri 4 orang, sang asisten galak mengatur hanya 2 orang 
yang dia toleransi bisa terlambat. Lalu masing-masing praktikan ada yang datang -2 
menit dimulai, ada yang -1 menit dimulai, ada yang tepat waktu dan satunya lebih 2 
menit, maka asistensi tetap dilaksanakan karena hanya satu orang yang terlambat.

- Pada pertemuan kedua, dihadiri 4 praktikan juga, asisten galak ingin batas 1 orang saja 
yang bisa terlambat. Masing-masing praktikan ada yang datang -5 menit dimulai, ada 
yang datang pas asistensi dimulai (0 menit), ada yang lebih 1 menit, ada yang lebih 3 
menit, maka asistensi dibatalkan karena ada 2 orang yang terlambat menghadiri jadwal 
yang ditentukan oleh asisten galak tersebut.
"""

def asistengalak(particpantlist,batas):
    datang_awal = [i for i in particpantlist if i <= 0]
    if len(datang_awal) >= batas:
        return "DILANJUTKAN"
    elif len(datang_awal) < batas:
        return "DIBATALKAN"

list_keterlambatan = [[2],
[4 ,3],
[-1, -3, 4, 2],
[6, 4],
[0 ,-1, 2, 0, 0, -5]]

n = (len(list_keterlambatan))

for lis in list_keterlambatan:
    print(asistengalak(lis,2))