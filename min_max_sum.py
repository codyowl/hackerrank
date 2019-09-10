#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
	sor = sorted(arr)
	mns = sum(sor[1:]) # removing minimum value of the sorted list
	mxs = sum(sor[:-1]) # removing maximum value of the sorted list
	print mxs, mns

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
