#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from collections import Counter
from functools import reduce
from operator import mul, concat

filename = "input9"
file = open(filename, 'r')
lines = [list(map(int, l.split(" "))) for l in file.readlines()]
file.close()

nums = []

for l in lines:
    r = [l]
    i = 0
    while sum(r[i]) != 0:
        r.append([r[i][j + 1] - r[i][j] for j in range(len(r[i]) - 1)])
        i += 1
    r = r[::-1]
    for i in range(1, len(r)):
        r[i].append(r[i - 1][-1] + r[i][-1])
    nums.append(r[-1][-1])

print(sum(nums))
    


