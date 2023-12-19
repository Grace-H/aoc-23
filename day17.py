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

def astar(grid):
    # Node - current x,y, cumulative heat loss, dir moved from, steps from that dir
    N = namedtuple("N", ["i", "j", "dir", "dir_count", "cost_so_far"])
    shortest = dict()
    tried = [[dict() for _ in grid[0]] for _ in grid] # (dir, dir_count) -> cost
    end = (len(grid) - 1, len(grid[0]) - 1)

    # Start PQ
    queue = PriorityQueue()

    # Change first vertex
    queue.put(PItem(0, N(0,0,(0,0),0,0)))
    shortest[(0,0)] = 0
    tried[0][0][((0,0),0)] = 0

    count = 0
    while not queue.empty():
        count += 1
        pitem = queue.get()
        pos = pitem.item
        cost = pitem.priority

        print("just got", pos.i, pos.j, "at", cost)
        # Last one
        if (pos.i, pos.j) == end:
            print(pos.cost_so_far)
            return

        # Try moving in all directions
        moves = []
        if pos.dir != North:
            moves.append(S)
        if pos.dir != E:
            moves.append(W)
        if pos.dir != S:
            moves.append(North)
        if pos.dir != W:
            moves.append(E)

        for m in moves:
            i = pos.i + m[0]
            j = pos.j + m[1]

            # check reachability
            if i < 0 or i > end[0]:
                continue
            if j < 0 or j > end[1]:
                continue
            dir_count = 0
            if m == pos.dir:
                dir_count = pos.dir_count + 1
                print("dir_count", dir_count)
            if dir_count > 2:
                continue

            # Update costs for each
            # Account for multiple ways to each node
            print("i", i, "j", j, end, len(grid))
            m_cost = pos.cost_so_far + grid[i][j]

            # if (i,j) not in shortest or shortest[(i,j)] > m_cost:
            #    shortest[(i,j)] = m_cost
            
            new_node = N(i, j, m, dir_count, m_cost)
            if (m, dir_count) not in tried[i][j] or tried[i][j][(m, dir_count)] > m_cost:
                tried[i][j][(m, dir_count)] = m_cost
                queue.put(PItem(m_cost + abs(i - end[0]) + abs(j - end[1]), new_node))
                print(new_node, "at", m_cost + abs(i - end[0]) + abs(j - end[1]))
                    
    else:
        print("loop term")


filename = "input17"
# filename = "test17"
file = open(filename, 'r')
lines = [list(map(int, list(l.strip()))) for l in file.readlines()]
file.close()

print(lines)
for l in lines:
    print(len(l))
astar(lines[:-1])
