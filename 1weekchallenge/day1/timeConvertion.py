"""
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.

    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
time_mapper = {
    '01': '13',
    '02': '14',
    '03': '15',
    '04': '16',
    '05': '17',
    '06': '18',
    '07': '19',
    '08': '20',
    '09': '21',
    '10': '22',
    '11': '23',
    '12': '00',
}


def timeConversion(s):
    time = s[:-2].split(':')
    AM_PM = s[len(s) - 2:len(s)]
    if AM_PM == 'AM':
        if time[0] == '12':
            time[0] = '00'
    else:
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)

    return ':'.join(time)


if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
