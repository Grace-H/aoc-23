#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from collections import Counter
from functools import reduce
from operator import mul, concat
import networkx as nx

def strparse(lines):
    p = compile("Game {:d}: {}\n")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "input10"
# filename = "test8"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

start = (0,0)
edges = []
l = len(lines) - 1
for i,x in enumerate(lines):
    k = len(x) - 1
    for j,y in enumerate(x):
        if y == "S":
            start = (i,j)
        if y =="|":
            if i > 0:
                edges.append(((i,j), (i - 1, j)))
            if i < l:
                edges.append(((i,j), (i + 1, j)))
        elif y == "-":
            if j > 0:
                edges.append(((i,j), (i, j - 1)))
            if j < k:
                edges.append(((i,j), (i, j + 1)))
        elif y == "L":
            if i > 0:
                edges.append(((i,j), (i - 1, j)))
            if j < k:
                edges.append(((i,j), (i, j + 1)))
        elif y == "J":
            if i > 0:
                edges.append(((i,j), (i - 1, j)))
            if j > 0:
                edges.append(((i,j), (i, j - 1)))
        elif y == "7" or y == "S":  # hard coded S val for input
            if y == "S":
                print("inserting S", i, j)
            if j > 0:
                edges.append(((i,j), (i, j - 1)))
            if i < l:
                edges.append(((i,j), (i + 1, j)))
        elif y == "F": # or y == "S": # hard coded S val for test
            if i < l:
                edges.append(((i,j), (i + 1, j)))
            if j < k:
                edges.append(((i,j), (i, j + 1)))

# Find longest cycle
G = nx.DiGraph(edges)
cycles = sorted(nx.simple_cycles(G), key=lambda x: len(x))
print(len(cycles[-1]) / 2)
