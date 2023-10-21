"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string 
"""
 
def longestCommonPrefix(strs):
    hasil = [sorted(x) for x in strs]
    return (hasil)










print(longestCommonPrefix(["flower","flow","flight"]))
# Ex
# ample 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 