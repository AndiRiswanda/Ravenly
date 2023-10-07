"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

"""

def Anagram(s,t):
   
    s_bersih = ("".join([x.lower() for x in s if x.isalnum()]))
    t_bersih = ("".join([x.lower() for x in t if x.isalnum()]))
    if len(s_bersih) != len(t_bersih):
    
        return False
    
    else:
        if sorted(s_bersih) == sorted(t_bersih):
            return True
        else :
            return False
        