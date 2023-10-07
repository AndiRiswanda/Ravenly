'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

'''

def arraydouble(ListOfNum):
    
    dicListOfNum = {x : 0 for x in ListOfNum}
    
    return not len(dicListOfNum) == len(ListOfNum)

print(arraydouble([1,2,3,4]))