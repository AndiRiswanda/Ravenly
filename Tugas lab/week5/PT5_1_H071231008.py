def stringCampuran(kata1,kata2):
    try:

        if len(kata1) != len(kata2):
            raise IndexError

        panjang = len(kata1)

        kataHasil = ""

        for i in range (panjang):
            kataHasil += kata1[i] + kata2[panjang-i-1]
        return kataHasil

    except TypeError: return "Input Invalid"

    except IndexError: return "kata Harus Sama Panjang"

"""
TestCase

"""

print(stringCampuran(kata1="ABC", kata2="xyz"))

print(stringCampuran(kata1="cilok", kata2="12345"))

print(stringCampuran(kata1="Hel", kata2="123"))

print(stringCampuran(kata1="abc", kata2="CBA"))

print(stringCampuran(kata1="abc", kata2="CBAA"))