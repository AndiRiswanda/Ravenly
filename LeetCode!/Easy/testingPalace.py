
''''
unsolved
'''

# import math
# import os
# import random
# import re
# import sys

# def diagonalDifference(arr):
#     topel= sum(tuple(arr[0[0]::4[0]]))
#     topel2= sum(tuple(arr[-3[0]:-8[0]:-2[0]]))
#     hasil = topel + topel2
#     if hasil < 0:
#         hasil = -hasil
#         return (hasil)
#     else :
#         return  hasil 



# arr= ([[11], [2],[4],
#             [4], [5], [6],
#             [10] ,[8], [-112]])



# def miniMaxSum(arr):
#    maximum = (arr[1:])
#    minimum = (arr[0:4])
#    print (f"{minimum} {maximum}")

# miniMaxSum([7 ,69, 2 ,221 ,8974])

# a = 1
# b = 2
# c = 3


# while a < 5:
#     a += 1
#     for d in range (b):
#         print (a)





jenis = ["Apple", "Nenas", "Tomat"]
nama = ["buah", "sayuran" ]

for x in jenis:
    if x != "Tomat":
        for y in nama[0:1]:
            print (y, x)
    elif x == "Tomat":
        for y in nama[1:2]:
            print (y, x)
