def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def pangkat (x,n):
   if n < 1:
       return 1
   else :
      return x * pangkat(x,n-1)

try:
    print(1 / 2)
except ZeroDivisionError:
    print ("tidak boleh sama dengan nol")
else:
    print("else tetap ter print")
finally:
    print("ini selalu berjalan")