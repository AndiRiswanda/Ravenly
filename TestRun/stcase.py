
n = 5
for i in range(1,n+1):
    print(" "*(n-i),end = "")
    print("#"*(i),end = "")
    print("#"*(i-1))



def primenumber(z):
    if z <= 2:
        return False
    else:
        for i in range(2,z):
            if z % i == 0:
                return False
    
    return True

print(primenumber(9223372036854775807))