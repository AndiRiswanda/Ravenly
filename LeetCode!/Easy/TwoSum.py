from collections import defaultdict as dl
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
 and you may not use the same element twice.
You can return the answer in any order.
"""
nums = [2,7,11,15,20,30]
target = 9


def twoSum(nums, target):
    hasil = []
    sumation = {}
    for index,value in enumerate(nums):
        sebelumnya = {}
        Range = target-value
        sumation[value] = index
        
    return hasil

    
            

        

        
# (twoSum([3,3],5))
# print("\n"*3)
print(twoSum([2,11,15,20,7,30],9))
print(twoSum([3,3],6))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))