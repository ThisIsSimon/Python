#https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    dictionary = {}
    score = [0, 0]
    for i in range(len(a)):
        dictionary[a[i]] = b[i]
        if a[i] > dictionary[a[i]]:
            score[0] += 1
        elif a[i] < dictionary[a[i]]:
            score[1] += 1
    return score    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
