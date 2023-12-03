#!/usr/bin/env python3

from parse import compile
from itertools import repeat

def strparse(lines):
    p = compile("Game {:d}: {}\n")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "input4"
# filename = "test4"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

lines = strparse(lines)
print(lines)

nums = []
for l in lines:
    print(i[1])

print(sum(nums))
