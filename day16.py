#!/usr/bin/env python3

from collections import namedtuple

filename = "input16"
# filename = "test16"
file = open(filename, 'r')
lines = [list(l.strip()) for l in file.readlines()]
file.close()

trans = {".": lambda i,j: (i,j),
         "/": lambda i,j: (-j, -i),
         "\\": lambda i,j: (j, i)
         }

B = namedtuple("Beam", ["i", "j", "di", "dj"])
edges = []
for j in range(len(lines[0])):
    edges.append(B(0,j,1,0))
    edges.append(B(len(lines) - 1, j, -1, 0))
for i in range(len(lines)):
    edges.append(B(i,0,0,1))
    edges.append(B(i, len(lines[0]) - 1, 0, -1))

eners = []
for e in edges:
    grid = [[[] for c in l] for l in lines]
    # Unprocessed beam locations - not crossed off in grid
    beams = []
    beams.append(e)

    while len(beams) > 0:
        i,j,di,dj = beams.pop()
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            continue
        if (di, dj) in grid[i][j]:
            continue
        grid[i][j].append((di,dj))
        if lines[i][j] == "|":
            if dj:
                beams.append(B(i - 1, j, -1, 0))
                beams.append(B(i + 1, j, 1, 0))
            else:
                beams.append(B(i + di, j, di, dj))
        elif lines[i][j] == "-":
            if di:
                beams.append(B(i, j - 1, 0, -1))
                beams.append(B(i, j + 1, 0, 1))
            else:
                beams.append(B(i, j + dj, di, dj))
        else:
            newdi, newdj = trans[lines[i][j]](di, dj)
            beams.append(B(i + newdi, j + newdj, newdi, newdj))

    ener = 0
    for l in grid:
        for g in l:
            if len(g) > 0:
                ener += 1
    eners.append(ener)
    print(ener)

print(max(eners))

