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

boxes = [[] for _ in range(256)]
for l in lines[0].strip().split(","):
    print(boxes)
    y = 0
    box = "" 
    focal = 0
    remove = True
    if '=' in l:
        box, focal = l.split("=")
        focal = int(focal)
        remove = False
    if '-' in l:
        box = l[0:-1]
    for x in box:
        y += ord(x)
        y *= 17
        y = y % 256
    if remove:
        for i in range(len(boxes[y])):
            if boxes[y][i][0] == box:
                del boxes[y][i]
                break
    else:
        for i in range(len(boxes[y])):
            if boxes[y][i][0] == box:
                boxes[y][i] = (box, focal)
                break
        else:
            print("adding")
            boxes[y].append((box, focal))

print(boxes)
a = []
for i,bucket in enumerate(boxes):
    for j,b in enumerate(bucket):
        a.append((i + 1) * (j + 1) * b[1])

print(a)
print(sum(a))




