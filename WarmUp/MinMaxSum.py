#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    s = [0] * len(arr)
    for i in range(len(arr)):
        s[i] = sum - arr[i]
    for i in range(len(s)):
        Minimum = min(s)
        Maximum = max(s)
    print(format(Minimum) + " " + format(Maximum))  

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
