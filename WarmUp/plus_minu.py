#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    countP = countN = countZ =0
    for i in range(n):
        if arr[i] > 0:
            countP += 1
        elif arr[i] < 0:
            countN +=1
        elif arr[i] == 0:
            countZ +=1
    print(format(countP/n) + "\n" + format(countN/n) + "\n" + format(countZ/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
