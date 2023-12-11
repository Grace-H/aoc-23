#!/usr/bin/env python3

from itertools import combinations
import numpy as np

filename = "input11"
#filename = "test11"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
lines = np.array([list(l.strip()) for l in lines])
file.close()

# expand universe
for i,l in enumerate(lines[::-1]):
    if not '#' in l:
        to_insert = np.array(['.' for i in range(len(l))])
        lines = np.insert(lines, len(l) - i, to_insert, axis=0)

for i in range(len(lines[0]) - 1, 0, -1):
    if not '#' in lines[:, i]:
        to_insert = np.array(['.' for i in range(len(lines))])
        lines = np.insert(lines, i, to_insert, axis=1)

# find nodes
nodes = []
for i,x in enumerate(lines):
    for j,y in enumerate(x):
        if y == '#':
            nodes.append((i,j))

# calc distances
dists = []
for x,y in combinations(nodes,2):
    dists.append(abs(x[0] - y[0]) + abs(y[1] - x[1]))

print(sum(dists))
