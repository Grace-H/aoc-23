#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from functools import reduce
from operator import mul, concat

def strparse(lines):
    p = compile("{}:          {:d} {:d} {:d} {:d}")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "input6"
# filename = "test4"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

time = list(map(int, lines[0].split(':')[1].strip().split()))
dist = list(map(int, lines[1].split(':')[1].strip().split()))
time = int(reduce(concat, list(map(str, time))))
dist = int(reduce(concat, list(map(str, dist))))


print(time, dist)

count = 0
for i in range(0, time):
    speed = i
    traveled = speed * (time - i)
    if traveled > dist:
        count += 1

print(count)
