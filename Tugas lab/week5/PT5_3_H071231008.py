def Anagram(kata1,kata2):
    try:

        kata1_bersih = ("".join([x.lower() for x in kata1 if x.isalnum()]))
        kata2_bersih = ("".join([x.lower() for x in kata2 if x.isalnum()]))

        if len(kata1_bersih) != len(kata2_bersih):
        
            return False
        
        else:
            if sorted(kata1_bersih) == sorted(kata2_bersih):
                return True
            else :
                return False
            
    except TypeError: return "Input Tidak Valid"


"""
testcase

"""
print(Anagram(kata1 = "aku suka", kata2 = "cilok" ))

print(Anagram(kata1 = "Binary", kata2 = "Brainy" ))

print(Anagram(kata1 = "Mother-in-law" , kata2 = "Woman lerHit"))

print(Anagram(kata1 = "rat", kata2 = "tar" ))

print(Anagram(kata1 = "I am Lord Voldemort", kata2 = "Tom Marvolo Riddle"))

print(Anagram(kata1 = "Astronomer", kata2 = "Moon Starer" ))
