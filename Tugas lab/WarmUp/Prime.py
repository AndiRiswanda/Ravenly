def prime_valid(n):
    """mengecek apakah N itu 
    adalah prime number"""   
    if n <= 1:
        return False
    else:
        for i in range (2 , n):
            if n % i == 0:
                return False
    return True
        
print(prime_valid(5))


def power(x,y):
    if y == 1:
        return y
    x * pow(y)
    y - 1

print(pow(2,4))