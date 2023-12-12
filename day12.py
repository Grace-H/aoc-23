#!/usr/bin/env python3

from collections import namedtuple
from operator import concat
from functools import reduce
from queue import LifoQueue

N = namedtuple("N", ["l", "nums", "i"])

def dfs(line):
    count = 0
    s = LifoQueue()
    s.put(N(line[0], line[1], 0))
    while not s.empty():
        n = s.get()
        i = n.i
        while i < len(n.l) and n.l[i] != '?':
            i += 1
        if i >= len(n.l):
            string = list(filter(lambda s: s != '', reduce(concat, n.l).split('.')))
            invalid = 1
            if len(string) != len(n.nums):
                invalid = 0
            else:
                for x,m in zip(string, n.nums):
                    if len(x) != m:
                        invalid = 0
            count += invalid
        else:
            l1 = list(n.l)
            l1[i] = '.'
            s.put(N(l1, n.nums, i))
            n.l[i] = '#'
            s.put(N(n.l, n.nums, i))
    return count

filename = "input12"
# filename = "test12"
file = open(filename, 'r')
lines = [l.strip().split(" ") for l in file.readlines()]
lines = list(map(lambda l: [list(l[0]), list(map(int, l[1].split(",")))], lines))
file.close()

count = 0
for l in lines:
    count += dfs(l)

print(count)

