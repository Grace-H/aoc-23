#!/usr/bin/env python3

from parse import compile
from itertools import repeat

def strparse(lines):
    p = compile("{:d} {:d} {:d}")
    return map(getattr, map(p.parse, lines), repeat('fixed'))

filename = "input5"
# filename = "test5"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

seeds = list(map(int, lines[0].strip().split()[1:]))

i = 3

stos = []
stof = []
while lines[i] != '\n':
    mapping = list(map(int, lines[i].strip().split()))
    stos.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1

i += 2
stof = []
while lines[i] != '\n':
    mapping = list(map(int, lines[i].strip().split()))
    stof.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1
i += 2

# f to w
ftow = []
while lines[i] != '\n':
    mapping = list(map(int, lines[i].strip().split()))
    ftow.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1
i += 2

# w to light
wtol = []
while lines[i] != '\n':
    mapping = list(map(int, lines[i].strip().split()))
    wtol.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1
i += 2

# l to t
ltot = []
while lines[i] != '\n':
    mapping = list(map(int, lines[i].strip().split()))
    ltot.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1
i += 2

# t to h
ttoh = []
while lines[i] != '\n':
    mapping = list(map(int, lines[i].strip().split()))
    ttoh.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1
i += 2

# h to l
htol = []
while i < len(lines):
    mapping = list(map(int, lines[i].strip().split()))
    htol.append((mapping[1], mapping[1] + mapping[2], mapping[0]))
    i += 1

mappings = {}
for s in stos:
    # Divide range?
    for i in range(s[0], s[1]):
        l = i
        l = s[2] + l - s[0]
        for x in stof:
            if x[0] <= l and x[1] > l:
                l = x[2] + l - x[0]
                break
        for x in ftow:
            if x[0] <= l and x[1] > l:
                l = x[2] + l - x[0]
                break
        for x in wtol:
            if x[0] <= l and x[1] > l:
                l = x[2] + l - x[0]
                break
        for x in ltot:
            if x[0] <= l and x[1] > l:
                l = x[2] + l - x[0]
                break
        for x in ttoh:
            if x[0] <= l and x[1] > l:
                l = x[2] + l - x[0]
                break
        for x in htol:
            if x[0] <= l and x[1] > l:
                l = x[2] + l - x[0]
                break
        mappings[i] = l

final = []
for k in range(0, len(seeds), 2):
    for s in range(seeds[k], seeds[k] + seeds[k + 1]):
        final.append(mappings[s])

print(min(final))
