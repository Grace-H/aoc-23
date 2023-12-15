#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from collections import Counter
from functools import reduce
from operator import mul, concat
import numpy as np

filename = "input15"
# filename = "test15"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

print(lines)

c = 0
for l in lines[0].strip().split(","):
    y = 0
    for x in l:
        y += ord(x)
        y *= 17
        y = y % 256
    c += y
print(c)

