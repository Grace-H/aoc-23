#!/usr/bin/env python3

from matplotlib import path

filename = "cycle10"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

# Path
cycle = list(map(lambda c: c.strip("()"), lines[0].strip("\n[]").split(", ")))
cycle = [[int(cycle[i]), int(cycle[i + 1])] for i in range(0, len(cycle), 2)]
P = path.Path(cycle)

filename = "input10"
file = open(filename, 'r')
lines = file.readlines()
file.close()

# Points to test if in path - remove cycle points because undef. behavior
test_points = [[i, j] for j in range(len(lines[0])) for i in range(len(lines))]
for c in cycle:
    test_points.remove(c)

enclosed = P.contains_points(test_points)

print((enclosed == True).sum())
