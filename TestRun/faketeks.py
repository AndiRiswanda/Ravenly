input_string = input("Masukkan sebuah string panjang: ")
length = len(input_string)
if length >= 3:
    part1 = input_string[:length//3]
    part2 = input_string[length//3:2*(length//3)]
    part3 = input_string[2*(length//3):]
    print("Bagian 1:", part1)
    print("Bagian 2:", part2)
    print("Bagian 3:", part3)
else:
    print("Panjang string terlalu pendek untuk dipotong.")


input_phrase = input("Masukkan sebuah kalimat atau frasa: ")
words = input_phrase.split()
acronym = ''.join(word[0].upper() for word in words)
print("Akronim:", acronym)

#split akan menjadi list jika tidak ada

def censor_bad_words(sentence, bad_words):
    for word in bad_words:
        sentence = sentence.replace(word, '*' * len(word))
    return sentence

bad_words = ["kotor", "kasar", "tidak pantas"]
input_sentence = input("Masukkan sebuah kalimat: ")
censored_sentence = censor_bad_words(input_sentence, bad_words)
print("Kalimat setelah disensor:", censored_sentence)                 


def are_anagrams(str1: str, str2: str) -> bool:
    # Remove spaces and convert both strings to lowercase
    str1 = ''.join(str1.split()).lower()
    str2 = ''.join(str2.split()).lower()

    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
print(are_anagrams("Astronomer", "Moon starer"))  # True
print(are_anagrams("Listen", "silent"))  # True (case-insensitive)

def Bold(kata):
    print (f"\033[05m{kata}\033[0m")

Bold("Andi Riswanda")


def katadepan(kata):
    a,b = kata.split()
    a = a[0:1].upper()
    b = b[0:1].upper()
    return (f"{a}{b}")

print(katadepan("Artifical Inteligence"))
