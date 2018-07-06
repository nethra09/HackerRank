#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sumL = sumR = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sumL += arr[i][j]
            if i+j == n-1:
                sumR += arr[i][j]
    difference = abs(sumL - sumR)
    
    return difference
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
