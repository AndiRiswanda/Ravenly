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


# def twoSum(nums, target):
#     hasil = {}
#     for i in range (len(nums)):
#         for j in range (i+1,len(nums)):
#             hasil[(nums[i] + nums[j])] = [i,j]
#     return hasil[target]

def twoSum(nums, target):
    hasil = {}
    for i in range(len(nums)):
        cari = target - nums[i]
        if cari in hasil:
            return [hasil[cari],i]
        else:
            hasil[nums[i]] = i




print(twoSum([2,11,15,20,7,30],9),"\n")

print(twoSum([3,3],6),"\n")
print(twoSum([3,2,4],6),"\n")
