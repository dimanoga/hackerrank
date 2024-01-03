"""
    Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly
    four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
    long integers.

    arr = [1,3,5,7,9]
    min = 1 + 3 + 5 + 7 = 16
    max = 3 + 5 + 7 + 9 = 24

"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    print(f'{sum(arr[:len(arr) - 1])} {sum(arr[1:])}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
