#!/usr/bin/env python3

import sys
from collections import Counter, namedtuple
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PItem:
    priority: int
    item: Any=field(compare=False)


Dir = namedtuple("Dir", ["i", "j"])
North = Dir(-1, 0)
S = Dir(1, 0)
E = Dir(0, 1)
W = Dir(0, -1)

def dfs(grid):
    # Node - current x,y, cumulative heat loss, dir moved from, steps from that dir
    N = namedtuple("N", ["i", "j", "dir", "dir_count"])
    relaxed = [[False for l in x] for x in grid]
    items = [[PItem(sys.maxsize, [N(i, j, None, None)]) for j,l in enumerate(grid[0])] for i,x in enumerate(grid)]

    # Start PQ
    stack = []
    for lists in items:
        for x in lists:
            stack.append(x)

    # Change first vertex
    items[0][0].priority = 0
    items[0][0].item = [N(0,0,(0,0),0)]

    count = 0
    while len(stack) > 0:
        count += 1
        pitem = stack[0]
        del stack[0]
        pos = pitem.item
        print(pos)
        relaxed[pos[0].i][pos[0].j] = True
        cost = pitem.priority

        print("just got", pos[0].i, pos[0].j, "at", cost)
        # Last one
        if pos[0].j == len(grid[0]) - 1 and pos[0].i == len(grid) - 1:
            for k in range(len(items)):
                print(list(map(lambda x: x.priority, items[k])))
 
            print(cost)
            return

        # Try moving in all directions
        for p in pos:
            moves = []
            if p.dir != North:
                moves.append(S)
            if p.dir != E:
                moves.append(W)
            if p.dir != S:
                moves.append(North)
            if p.dir != W:
                moves.append(E)

            for m in moves:
                i = p.i + m[0]
                j = p.j + m[1]

                # check reachability
                if i < 0 or i >= len(grid):
                    continue
                if j < 0 or j >= len(grid[0]):
                    continue
                dir_count = 0
                if m == p.dir:
                    dir_count = p.dir_count + 1
                    print("dir_count", dir_count)
                if dir_count > 2:
                    continue

                # Update costs for each
                # Account for multiple ways to each node
                if not relaxed[i][j] and items[i][j].priority == grid[i][j] + cost:
                    found = False
                    for z, it in enumerate(items[i][j].item):
                        print(it.dir, m, dir_count)
                        if it.dir == m:
                            found = True
                            # Shorter from this direction
                            if it.dir_count > dir_count:
                                items[i][j].item[z] = N(i, j, m, dir_count)
                                print("found a shorter way", i, j, m, dir_count, items[i][j].priority)
                    if not found:
                        print("adding another way to", i, j, m, dir_count, items[i][j].priority)
                        items[i][j].item.append(N(i, j, m, dir_count))
                elif not relaxed[i][j] and items[i][j].priority > grid[i][j] + cost:
                    items[i][j].priority = grid[i][j] + cost
                    items[i][j].item = [N(i, j, m, dir_count)]
                    print("adjusting cost of", i, j, m, dir_count, items[i][j].priority)
                    # Update "priority queue"
                    for ii, it in enumerate(stack):
                        if it.item[0].i == i and it.item[0].j == j:
                            del stack[ii]
                            break
                    for ii, it in enumerate(stack):
                        if items[i][j].priority < it.priority:
                            stack.insert(ii, items[i][j])
                            break
                    
    else:
        print("loop term")
        print(len(stack))


filename = "input17"
filename = "test17"
file = open(filename, 'r')
lines = [list(map(int, list(l.strip()))) for l in file.readlines()]
file.close()

dfs(lines)
