# def prime_valid(n):
#     """mengecek apakah N itu 
#     adalah prime number"""   
#     if n <= 1:
#         return False
#     else:
#         for i in range (2 , n):
#             if n % i == 0:
#                 return False
#     return True
        
# print(prime_valid(8))

def prime (x):
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x*0.5 )+1)) 
print(prime(3))

def fpb(x,y):
    terbesar = max(x,y)
    while True:
        if x % terbesar == 0 and y % terbesar == 0:
            FPB = terbesar
            break
        terbesar -= 1
    return terbesar

def kpk(x, y):
    return (x*y) // fpb(x,y)

print(fpb(10,5))
print(kpk(10,5))