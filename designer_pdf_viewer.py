#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    word_height_dict = {}
    height_list = list(h)
    alphabets ="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabets)):
        word_height_dict[alphabets[i]] = height_list[i]
    words_height_list = []
    for w in word:
        words_height_list.append(word_height_dict[w])
    highest_word_height = max(words_height_list)
    return highest_word_height * len(word)           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
