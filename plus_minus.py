#!/bin/python
from __future__ import division
import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
	positive = 0
	negative = 0
	zero = 0
	for i in range(len(arr)):
		if arr[i] > 0:
			positive += 1
		elif arr[i] < 0:
			negative += 1
		elif arr[i] == 0:
			zero += 1   
	return positive, negative, zero         

if __name__ == '__main__':
	n = int(raw_input())

	arr = map(int, raw_input().rstrip().split())
	
	result = plusMinus(arr)
	print round(result[0]/n, 5)
	print round(result[1]/n, 5)
	print round(result[2]/n, 5)