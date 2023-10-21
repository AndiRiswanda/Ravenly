
from collections import defaultdict
'''
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
'''


strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



def groupAnagrams(strs):
    grouped = defaultdict(list)
    hasil = []
    for values in strs:
        sortedvalue = tuple(sorted(values))
        grouped[sortedvalue]
        (grouped[sortedvalue]).append(values)
    for i in grouped.values():
        hasil.append(i)
    return (hasil)
    


print(groupAnagrams(strs))