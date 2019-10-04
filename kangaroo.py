#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
	res = "NO"
	# This is my initial logic but this gives time exceed error for few test cases
	# if x2 > x1 and v2 > v1:
	# 	return res
	# while x1 != x2 and len(range(x1))<=10000:
	# 	x1 = x1 + v1
	# 	x2 = x2 + v2
	# 	if x1 == x2:
	# 		res = "YES"
	# 		break
	# return res

	###
	#changed to this logic after seeing on submission
	####
	if x1 > x2 and v2 > v1:
		return res
	else:
		if (x1 - x2) % (v2 - v1) == 0:
			res = "YES"
			return res	


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
