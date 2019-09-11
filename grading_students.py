#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    # formula is (number+ denominator-1)/denominator * denominator
    rounded_value = [int(round((data+4.0)/5.0)*5.0) for data in grades] 
    for i in range(len(rounded_value)):
        if grades[i] < 38:
            print (grades[i])
        else:    
            if rounded_value[i]-grades[i] < 3:
                print (rounded_value[i])
            else:
                print (grades[i])    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
