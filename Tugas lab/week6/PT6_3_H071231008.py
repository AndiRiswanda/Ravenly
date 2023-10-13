import random

listAngka = [random.randint(1, 100) for x in range (10)]

genap = [x for x in listAngka if x%2 == 0]
ganjil = [x for x in listAngka if x%2 != 0]
habis5 = [x for x in listAngka if x%5 == 0]

print (f"angka genap adalah : {genap}")
print (f"angka ganjil adalah :{ganjil}")
print (f"angka habis di bagi 5 adalah :{habis5}")