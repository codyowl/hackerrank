#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    length = len(arr[0])
    i = 0
    l_d = []
    r_d = []
    while i < length:
        l_d.append(arr[i][i])
        i += 1
    i = 0
    j = length - 1
    while i < length:
        r_d.append(arr[i][j])
        i += 1
        j -= 1  
    l_d_s = sum(l_d)
    r_d_s = sum(r_d)
    difference = abs(l_d_s-r_d_s)      
    return difference       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()