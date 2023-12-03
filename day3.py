#!/usr/bin/env python3

from parse import compile
from itertools import repeat

def strparse(lines):
    p = compile("Game {:d}: {}\n")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "input3"
# filename = "test3"
file = open('input3', 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

nums = []
print(lines)
syms = "!@#$%^&*()><?{}[]/|\\=_-+"
for i,l in enumerate(lines):
    num = ""
    for j,c in enumerate(l):
        if c.isdigit():
            num += c
        elif num != "":
            num1 = num
            num = ""
            found = False
            # search row above
            if i > 0:
                for k in range(j - 1 - len(num1) if j - 1 - len(num1) >= 0 else j - len(num1), j + 1):
                    if not found and lines[i - 1][k] in syms:
                        nums.append(int(num1))
                        found = True
            # search row below
            if i < len(lines) - 1:
                for k in range(j - 1 - len(num1) if j - 1 - len(num1) >= 0 else j - len(num1), j + 1):
                    if not found and lines[i + 1][k] in syms:
                        nums.append(int(num1))
                        found = True
            # front
            if not found and j - 1 - len(num1) >= 0 and lines[i][j - len(num1) - 1] in syms:
                nums.append(int(num1))
                found = True
            if not found and c in syms:
                nums.append(int(num1))
                found = True

print(nums)
print(sum(nums))
