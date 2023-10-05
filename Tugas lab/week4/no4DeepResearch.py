import time
import os

def clearscree():
    os.system("cls")
def catAndmouse1(cata,catb,ratc):
    if ratc > cata: 
        cat1 = -(cata - ratc)
    else:
        cat1 = (cata-ratc)
    if ratc > catb: 
        cat2 = -(catb - ratc)
    else:
        cat2 = (catb-ratc)

    if cat1 > cat2:
        print("cat B wins")
    elif cat1 == cat2:
        print("rat wins")
    else: print("cat A wins")

def catAndmouse2(cata,catb,ratc):
    cat1 = abs(cata - ratc)
    cat2 = abs(catb - ratc)

    if cat1 > cat2:
        print("cat B wins")
    elif cat1 == cat2:
        print("rat wins")
    else: print("cat A wins")

clearscree()
print("mengunakan if-else (long):")
start_time = time.perf_counter()
catAndmouse1(cata=19, catb=16, ratc=15)
end_time = time.perf_counter()
ifPanjang = end_time - start_time
print(f"dieksekusi dengan kecepatan : {ifPanjang:.6f} detik")

print("\nfungsi abs (short):")
start_time = time.perf_counter()
catAndmouse2(cata=19, catb=16, ratc=15)
end_time = time.perf_counter()
abspendek = end_time - start_time
print(f"dieksekusi dengan kecepatan : {abspendek:.6f} detik")

if abspendek < ifPanjang:
    print(f"\n(shortabs) Lebih cepat ")
else:
    print(f"\n(longIfElse) Lebih cepat ")
