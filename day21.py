#!/usr/bin/env python3

filename = "input21"
# filename = "test21"
file = open(filename, 'r')
lines = [list(l.strip()) for l in file.readlines()]
file.close()

si = 65
sj = 65

lines[si][sj] = '.'

nexts = [(si, sj)]
for l in range(64):
    n_nexts = list()
    for n in nexts:
        i,j = n
        # N
        if i - 1 >= 0 and lines[i - 1][j] == '.' and (i - 1, j) not in n_nexts:
            n_nexts.append((i - 1, j))
        if i + 1 < len(lines) and lines[i + 1][j] == '.' and (i + 1, j) not in n_nexts:
            n_nexts.append((i + 1, j))
        if j - 1 >= 0 and lines[i][j - 1] == '.' and (i, j - 1) not in n_nexts:
            n_nexts.append((i, j - 1))
        if j + 1 < len(lines[i]) and lines[i][j + 1] == '.' and (i, j + 1) not in n_nexts:
            n_nexts.append((i, j + 1))
    nexts = n_nexts.copy()

print(len(nexts))
