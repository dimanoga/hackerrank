"""
    Given an array of integers, where all elements but one occur twice, find the unique element.
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    x = 0
    for i in a:
        x ^= i
    return x


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
