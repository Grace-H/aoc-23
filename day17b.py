#!/usr/bin/env python3

from queue import PriorityQueue
from collections import namedtuple
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PItem:
    priority: int
    item: Any=field(compare=False)

def astar(grid):
    # Node - current x,y, cumulative heat loss, dir moved from, steps from that dir
    N = namedtuple("N", ["i", "j", "dir", "dir_count", "cost_so_far"])
    # Dir - represents possible move from current location
    Dir = namedtuple("Dir", ["i", "j"])
    North = Dir(-1, 0)
    S = Dir(1, 0)
    E = Dir(0, 1)
    W = Dir(0, -1)
    end = (len(grid) - 1, len(grid[0]) - 1)

    # Moves from each square that have been tried
    tried = [[dict() for _ in grid[0]] for _ in grid] # (dir, dir_count) -> cost

    # Start PQ
    queue = PriorityQueue()

    # Change first vertex
    queue.put(PItem(0, N(0,0,(0,0),0,0)))
    tried[0][0][((0,0),0)] = 0

    while not queue.empty():
        pitem = queue.get()
        pos = pitem.item
        cost = pitem.priority

        # Last one
        if (pos.i, pos.j) == end:
            print(pos.cost_so_far)
            return

        # Try moving in all directions
        moves = []
        if pos.dir[0] < 0:
            moves.append(North)
            moves.append((0,-4))
            moves.append((0,4))
        elif pos.dir[1] > 0:
            moves.append(E)
            moves.append((-4,0))
            moves.append((4,0))
        elif pos.dir[0] > 0:
            moves.append(S)
            moves.append((0,-4))
            moves.append((0,4))
        elif pos.dir[1] < 0:
            moves.append(W)
            moves.append((-4,0))
            moves.append((4,0))
        elif pos.dir == (0,0):
            moves.append((4,0))
            moves.append((0,4))

        for m in moves:
            i = pos.i + m[0]
            j = pos.j + m[1]

            # Update costs & push new node
            delta_i = 1 if m[0] != 0 else 0
            delta_i = -1 if m[0] < 0 else delta_i
            delta_j = 1 if m[1] != 0 else 0
            delta_j = -1 if m[1] < 0 else delta_j

            pos_i = 1 if pos.dir[0] != 0 else 0
            pos_i = -1 if pos.dir[0] < 0 else pos_i
            pos_j = 1 if pos.dir[1] != 0 else 0
            pos_j = -1 if pos.dir[1] < 0 else pos_j

            # check reachability
            if i < 0 or i > end[0]:
                continue
            if j < 0 or j > end[1]:
                continue
            dir_count = 4
            if (pos_i, pos_j) == (delta_i, delta_j):
                dir_count = pos.dir_count + 1
            if dir_count > 10:
                continue


            curr_i = pos.i + delta_i
            curr_j = pos.j + delta_j
            m_cost = pos.cost_so_far + grid[i][j]
            while curr_i != i or curr_j != j:
                m_cost += grid[curr_i][curr_j]
                curr_i += delta_i
                curr_j += delta_j

            new_node = N(i, j, m, dir_count, m_cost)
            if (m, dir_count) not in tried[i][j] or tried[i][j][(m, dir_count)] > m_cost:
                tried[i][j][(m, dir_count)] = m_cost
                queue.put(PItem(m_cost + abs(i - end[0]) + abs(j - end[1]), new_node))

filename = "input17"
# filename = "test17"
file = open(filename, 'r')
lines = [list(map(int, list(l.strip()))) for l in file.readlines()]
file.close()

astar(lines)
