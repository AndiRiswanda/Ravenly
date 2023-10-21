def romanToInt(s):
    roman = {
        0 : 0,
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    hasil = []
    for inx,val in enumerate(s):
        if inx == 0 :
            prev = val
        else:
            prev = s[inx-1]

        if roman[val] - roman[prev] > 0:
            hasil.append(roman[val]-roman[prev])
            hasil[hasil.index(roman[prev])] = 0
        else:
            hasil.append(roman[val])
    return sum(hasil)



# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.