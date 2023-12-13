#!/usr/bin/env python3

from collections import namedtuple
from operator import concat
from functools import reduce
from queue import LifoQueue
import re
import numpy as np

N = namedtuple("N", ["l", "li", "lsum", "p", "pi", "psum"])

def dfs(line):
    count = 0
    print(line)
    s = LifoQueue()

    # Search for large "boulders"
    # string = sorted(list(filter(lambda s: s != '', re.split("[?.]", reduce(concat, line[0])))), key=lambda a: len(a))
    # nums = sorted(line[1])

    # Push first node
    i = 0
    while i < len(line[0]) and line[0][i] == '.':
        i += 1
    s.put(N(line[0], i, 0, line[1], 0, sum(line[1]) + len(line[1]) - 1))

    while not s.empty():
        n = s.get()
        i = n.li
        pi = n.pi
        j = i
        lpatch = 0
        lsum = n.lsum
        psum = n.psum
        while j < len(n.l) and n.l[j] != '?' and pi < len(n.p):
            # Patch completion
            if n.l[j] == '.':
                if lpatch == n.p[pi]:
                    lsum += lpatch
                    psum -= lpatch
                    pi += 1
                    lpatch = 0
                elif lpatch != 0:
                    break
            else:
                if lpatch == 0:  # Start of new patch
                    i = j
                lpatch += 1
            j += 1
        else:  # Natural loop termination
            if j == len(n.l) or pi == len(n.p):
                if lpatch == 0 and pi == len(n.p):
                    count += 1
                elif pi == len(n.p) - 1 and lpatch == n.p[pi] and pi == len(n.p) - 1:
                    count += 1
            else:  # Generate next two nodes
                # # Node
                if lpatch + 1 <= n.p[pi] and psum - lsum <= len(n.l) - i:
                    l1 = list(n.l)
                    l1[j] = '#'
                    if lpatch == 0:  # start of new patch
                        i = j
                    s.put(N(l1, i, lsum, n.p, pi, psum))
                # . Node
                # if this completed a patch
                if lpatch == n.p[pi]:
                    lsum += lpatch
                    psum -= lpatch
                    pi += 1
                    i = j
                l1 = list(n.l)
                l1[j] = '.'
                while i < len(l1) and l1[i] == '.':
                    i += 1
                if psum - lsum > len(l1) - i:
                    continue
                s.put(N(l1, i, lsum, n.p, pi, psum))
    return count

filename = "input12"
# filename = "test12"
file = open(filename, 'r')
lines = [l.strip().split(" ") for l in file.readlines()]
file.close()
lines = [[((l[0] + '?') * 5)[:-1], ((l[1] + ',') * 5)[:-1]] for l in lines]
lines = list(map(lambda l: [list(l[0]), list(map(int, l[1].split(",")))], lines))

count = 0
# print(dfs(lines[5]))

for l in lines:
    total = dfs(l)
    print(total)
    count += total

#print(count)
