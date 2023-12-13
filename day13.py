#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from collections import Counter
from functools import reduce
from operator import mul, concat
import numpy as np

filename = "input13"
# filename = "test13"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

grids = []
g = []
for l in lines:
    if l == '\n':
        grids.append(np.array(g))
        g = []
    else:
        g.append(list(l.strip()))
grids.append(np.array(g))

total = 0
for g in grids:
    print("grid")
    found = False
    # check columns
    for i in range(1, len(g[0])):
        low = i - 1
        high = i
        while low >= 0 and high <= len(g[0]) - 1:
            if (np.equal(g[:, low], g[:, high])).all():
                low -= 1
                high += 1
            else:
                break
        else:
            total += i
            found = True
    # check rows
    for i in range(1, len(g)):
        low = i - 1
        high = i
        while low >= 0 and high <= len(g) - 1:
            if (np.equal(g[low, :], g[high, :])).all():
                low -= 1
                high += 1
            else:
                break
        else:
            total += i * 100
            found = True
    if not found:
        print("NOT FOUND\n", g)

print(total)
