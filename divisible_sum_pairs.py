#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
	# to get the index count
	index = [i for i in range(len(ar))]
	# to get all the index combination of 2
	index_combo = [index for index in list(combinations(index, 2))]
	# list comprehension to get the list of combination divisible by k
	divisible_pairs = [i for i in index_combo if i[0] < i[1]]
	count = 0
	
	for i in divisible_pairs:
		sum_value = ar[i[0]] + ar[i[1]]
		if sum_value % k == 0:
			count += 1

	return count		


	
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
