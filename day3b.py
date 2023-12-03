#!/usr/bin/env python3

from parse import compile
from itertools import repeat

def strparse(lines):
    p = compile("Game {:d}: {}\n")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "input3"
# filename = "test3"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

total = 0
print(lines)
syms = "!@#$%^&*()><?{}[]/|\\=_-+"
for i,l in enumerate(lines):
    num = ""
    for j,c in enumerate(l):
        if c == '*':
            print(i, j)
            nums = []
            max_above = i - 2
            max_below = i - 2
            # Left
            num = ""
            k = j - 1
            while k >= 0 and lines[i][k].isdigit():
                num = lines[i][k] + num
                k -= 1
            if num != "":
                nums.append(int(num))
            num = ""
            # right
            k = j + 1
            while k < len(l) and lines[i][k].isdigit():
                num += lines[i][k]
                k += 1
            if num != "":
                nums.append(int(num))
            num = ""
            # above
            if i > 0:
                num = ""
                k = j - 1 if j - 1 > 0 else 0
                while k > -1 and lines[i - 1][k].isdigit():
                    k -= 1
                while k <= j or lines[i - 1][k].isdigit():
                    if lines[i - 1][k] == '.':
                        if num != "":
                            nums.append(int(num))
                            num = ""
                    else:
                        num += lines[i - 1][k]
                    k += 1
                if num != "":
                    nums.append(int(num))
            # below
            if i < len(lines) - 1:
                num = ""
                k = j - 1 if j - 1 > 0 else 0
                while k > -1 and lines[i + 1][k].isdigit():
                    k -= 1
                while k <= j or lines[i + 1][k].isdigit():
                    if lines[i + 1][k] == '.':
                        if num != "":
                            nums.append(int(num))
                            num = ""
                    else:
                        num += lines[i + 1][k]
                    k += 1
                if num != "":
                    nums.append(int(num))
                    

            print(nums)
            if len(nums) == 2:
                print("gear", nums)
                total += nums[0] * nums[1]
print(total)
