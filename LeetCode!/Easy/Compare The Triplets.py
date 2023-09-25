#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

a = [17, 28, 30]
b = [99, 16, 8]


def compareTriplets(a, b):
    bobScore = 0
    alisaScore = 0
    if a[0] > b[0]:
        alisaScore += 1
    elif a[0] < b[0]:
        bobScore += 1
    if a[1] > b[1]:
        alisaScore += 1
    elif a[1] < b[1]:
        bobScore += 1
    if a[2] > b[2]:
        alisaScore += 1
    elif a[2] < b[2]:
        bobScore += 1
    else:
       pass

    return (f"{alisaScore} {bobScore}")

print (compareTriplets(a, b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
