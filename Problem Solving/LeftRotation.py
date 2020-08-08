/*
Given an array of n integers and a number,d , perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.

https://www.hackerrank.com/challenges/array-left-rotation/problem
*/

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(* a[d:] + a[:d]) //if you want to print list without the brackets, use *
