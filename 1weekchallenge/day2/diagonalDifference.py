"""
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    input:
    3

    11 2 4
    4 5 6
    10 8 -12

    output:

    15

    Explanation:
    11
       5
        -12
    11 + 5 - 12 = 4

         4
       5
    10

    4 + 5 + 10 = 19

    |4 - 19| = 15
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # return abs(sum([arr[i][i] - arr[i][-(i + 1)] for i in range(len(arr))]))

    # Считаем диагональ слева направо
    left_right_sum = 0
    for i in range(len(arr)):
        left_right_sum += arr[i][i]

    # Считаем диагональ справа налево
    right_left_sum = 0
    for j in range(len(arr)):
        right_left_sum += arr[j][len(arr) - j - 1]
    return abs(left_right_sum - right_left_sum)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
