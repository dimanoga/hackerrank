"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
 Print the decimal value of each fraction on a new line with  places after the decimal."""
# !/bin/python3

import math
import os
import random
import re
import sys
from decimal import *

getcontext().prec = 6


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def count_ratios(int_counts: Decimal, arr_len: int) -> Decimal:
    if int_counts == 0:
        return 0
    else:
        return int_counts / arr_len


def plusMinus(arr: list[int]):
    if len(arr) == 0:
        print(0)
        print(0)
        print(0)
        return

    positive = Decimal(0)
    negative = Decimal(0)
    zero = Decimal(0)
    for i in arr:
        if i > 0:
            positive += 1
        elif i == 0:
            zero += 1
        else:
            negative += 1
    print("{:.6f}".format(count_ratios(int_counts=positive, arr_len=len(arr))))
    print("{:.6f}".format(count_ratios(int_counts=negative, arr_len=len(arr))))
    print("{:.6f}".format(count_ratios(int_counts=zero, arr_len=len(arr))))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
