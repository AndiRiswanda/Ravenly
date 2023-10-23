"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.
 """

s1 = "abcabcbb"
s2 = "bbbbb"

def longsub(word):
    longsubdic = {}
    hasil = []

    for index,letter in enumerate(word):
        try:
            second = word[index+1]
            while True:
                if letter == second:
                    break
                else:
                    hasil.append(letter)
                    print (second)
                    break``
        except IndexError:
            pass


    return hasil


print(longsub(s1)) 
print("\n\n\n") 
print(longsub(s2)) 
print("\n\n\n") 

