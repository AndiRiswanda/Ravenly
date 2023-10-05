def palindrome(s):
    s = s.lower().replace(" ", "").strip(".,!?")
    return s == s[::-1]


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def anagrams(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
