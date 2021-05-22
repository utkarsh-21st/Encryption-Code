#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = ''.join(s.split())
    len_ = len(s)

    z = len_ ** 0.5
    n_row = math.floor(z)
    n_col = math.ceil(z)

    if n_row * n_col < len_:
        n_row += 1

    arr = [['' for i in range(n_col)] for j in range(n_row)]

    a = 0
    b = 0
    for j in range(n_row):
        b = n_col * (j+1)
        temp = s[a: b]
        for i in range(len(temp)):
            arr[j][i] = temp[i]
        a = b

    temps = []
    for i in range(n_col):
        temp = ''
        for j in range(n_row):
            temp += arr[j][i]
        temps.append(temp)

    out = ' '.join(temps)
    return out
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()