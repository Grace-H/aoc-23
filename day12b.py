#!/usr/bin/env python3

from collections import namedtuple
from operator import concat
from functools import reduce
from queue import LifoQueue

N = namedtuple("N", ["l", "li", "lsum", "p", "pi", "psum"])

def dfs(line):
    count = 0
    s = LifoQueue()

    # Push first node
    i = 0
    while i < len(line) and line[i] == '.':
        i += 1
    s.put(N(line[0], i, 0, line[1], 0, sum(line[1])))

    while not s.empty():
        n = s.get()
        i = n.li
        pi = n.pi
        j = i
        lpatch = 0
        lsum = n.lsum
        while j < len(n.l) and n.l[j] != '?' and pi < len(n.p):
            # print("pi", pi, "j", j, "lpatch", lpatch)
            # Patch completion
            if n.l[j] == '.':
                if lpatch == n.p[pi]:
                    lsum += lpatch
                    pi += 1
                    lpatch = 0
                    # print("pi", pi)
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
                    # # print("here", n.l)
                    count += 1
            else:  # Generate next two nodes
                # # Node
                if lpatch + 1 <= n.p[pi] and sum(n.p[pi:]) + len(n.p[pi:]) - 1 - lsum <= len(n.l) - i:
                    l1 = list(n.l)
                    l1[j] = '#'
                    if lpatch == 0:  # start of new patch
                        i = j
                    s.put(N(l1, i, n.lsum, n.p, pi, n.psum))
                    # print("added #", N(l1, i, n.lsum, n.p, pi, n.psum))
                # . Node
                # if this completed a patch
                # # print(n.p[pi])
                if lpatch == n.p[pi]:
                    lsum += lpatch
                    # print("incrementing pi to ", pi + 1)
                    pi += 1
                    i = j
                l1 = list(n.l)
                l1[j] = '.'
                # print("j", j, l1[j])
                while i < len(l1) and l1[i] == '.':
                    i += 1
                    # print("inc i to ", i, l1)
                if sum(n.p[pi:]) + len(n.p[pi:]) - 1 - lsum > len(l1) - i:
                    continue
                s.put(N(l1, i, lsum, n.p, pi, n.psum))
                # # print("added .", N(l1, i, n.lsum, n.p, pi, n.psum))
    return count

filename = "input12"
filename = "test12"
file = open(filename, 'r')
lines = [l.strip().split(" ") for l in file.readlines()]
file.close()
lines = [[((l[0] + '?') * 5)[:-1], ((l[1] + ',') * 5)[:-1]] for l in lines]
lines = list(map(lambda l: [list(l[0]), list(map(int, l[1].split(",")))], lines))

count = 0
# print(lines[0])
print(dfs(lines[0]))
for l in lines:
    total = dfs(l)
    print(total)
    count += total

print(count)
