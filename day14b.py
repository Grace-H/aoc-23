#!/usr/bin/env python3

filename = "input14"
# filename = "test14"
file = open(filename, 'r')
lines = [list(l.strip()) for l in file.readlines()]
file.close()

arrays = []
prev = [l[:] for l in lines]
for t in range(1000):
    for i,l in enumerate(lines):
        for j,o in enumerate(l):
            if o == 'O':
                # move it up
                k = i - 1
                while k >= 0 and lines[k][j] == '.':
                    lines[k][j] = 'O'
                    lines[k + 1][j] = '.'
                    k -= 1

    for i,l in enumerate(lines):
        for j,o in enumerate(l):
            if o == 'O':
                # move it left
                k = j - 1
                while k >= 0 and lines[i][k] == '.':
                    lines[i][k] = 'O'
                    lines[i][k + 1] = '.'
                    k -= 1

    for i,l in enumerate(lines[::-1]):
        for j,o in enumerate(l):
            if o == 'O':
                # move it down
                k = len(lines) - i
                while k < len(lines) and lines[k][j] == '.':
                    lines[k][j] = 'O'
                    lines[k - 1][j] = '.'
                    k += 1

    for i,l in enumerate(lines):
        for j,o in enumerate(l[::-1]):
            if o == 'O':
                # move it right
                k = len(l) - j
                while k < len(l) and lines[i][k] == '.':
                    lines[i][k] = 'O'
                    lines[i][k - 1] = '.'
                    k += 1

    if lines in arrays:
        cycle_start = arrays.index(lines)
        cycle_len = t - cycle_start
        num = (1000000000 - cycle_start) % cycle_len
        index = num + cycle_start - 1
        count = 0
        for i,l in enumerate(arrays[index][::-1]):
            for j in l:
                if j == 'O':
                    count += i + 1
        print(count)
        break
    arrays.append([l[:] for l in lines])
    prev = [l[:] for l in lines]
