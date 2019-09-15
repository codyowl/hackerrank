#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

""" 
logic
takeout value based on m-1
now add value one by one to a queue slicing rest of the value of m-1
check if the sum equals to d or not
if then increase the counter
pop the first element of the queue
"""

# Complete the birthday function below.
def birthday(s, d, m):
	# getting first value based on m
	valid = 0
	queue = s[:m-1]
	for data in s[m-1:]:
		queue.append(data)
		#checking if the value appended to the queue is equal to the sum of d
		if sum(queue) == d:
			valid += 1
		queue.pop(0)
	return valid		


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    
    fptr.write(str(result) + '\n')

    fptr.close()
