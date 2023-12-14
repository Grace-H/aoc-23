#!/usr/bin/env python3

filename = "input14"
# filename = "test14"
file = open(filename, 'r')
lines = [list(l) for l in file.readlines()]
file.close()

for i,l in enumerate(lines):
    for j,o in enumerate(l):
        if o == 'O':
            # move it up
            k = i - 1
            while k >= 0 and lines[k][j] == '.':
                lines[k][j] = 'O'
                lines[k + 1][j] = '.'
                k -= 1

count = 0
for i,l in enumerate(lines[::-1]):
    for j in l:
        if j == 'O':
            count += i + 1
print(count)
