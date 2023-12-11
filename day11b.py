#!/usr/bin/env python3

from itertools import combinations
import numpy as np

filename = "input11"
# filename = "test11"
file = open(filename, 'r')
lines = file.readlines()
lines = np.array([list(l.strip()) for l in lines])
file.close()

# expand universe
rows = []
for i,l in enumerate(lines[::-1]):
    if not '#' in l:
        rows.append(len(l) - i - 1)
rows = np.array(rows)

cols = []
for i in range(len(lines[0]) - 1, 0, -1):
    if not '#' in lines[:, i]:
        cols.append(i)
cols = np.array(cols)

nodes = []
for i,x in enumerate(lines):
    for j,y in enumerate(x):
        if y == '#':
            nodes.append((i,j))

dists = []
for x,y in combinations(nodes,2):
    ydir = abs(x[0] - y[0])
    smaller = min([x[0], y[0]])
    larger = max([x[0], y[0]])
    ydir += 999999 * ((smaller < rows) & (rows < larger)).sum()
    xdir = abs(x[1] - y[1])
    smaller = min([x[1], y[1]])
    larger = max([x[1], y[1]])
    xdir += 999999 * ((smaller < cols) & (cols < larger)).sum()
    dists.append(xdir + ydir)

print(sum(dists))
