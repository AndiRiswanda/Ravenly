def faktorial(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
      return n * faktorial (n-1)

'''
P(n, r)= n! / (n-r)!
'''

def permutasi(n,r):
    if 1 <= r <= 30 and 1 <= n <= 30:
        if n-r < 0:
            return 0
        else:
            return (faktorial (n) // faktorial(n-r))
    else:
        print ("nomor tidak valid")


usput1, usput2 = (input()).split()
usput1 = int(usput1)
usput2 = int(usput2)

print (permutasi(usput1,usput2))