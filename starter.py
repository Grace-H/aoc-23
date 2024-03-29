#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from collections import Counter
from functools import reduce
from operator import mul, concat
import numpy as np

def strparse(lines):
    p = compile("Game {:d}: {}\n")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "inputXX"
# filename = "testXX"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

print(lines)

for l in lines:
    print(l)
