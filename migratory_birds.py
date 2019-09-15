#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds = [1,2,3,4,5]
    bird_dict = {}
    for b in birds:
        bird_dict[b] = [data for data in arr if data==b]
    for key in bird_dict:
        bird_dict[key] = len(bird_dict[key])
    max_bird = max(bird_dict.values())
    for key, value in bird_dict.items():
        if value == max_bird:
            print (key)
            break   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
