#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from queue import Queue

def strparse(lines):
    p1 = compile("Card   {:d}: {} | {}")
    print(p.parse(lines[0]))
    return map(p.parse, lines)

filename = "input4"
# filename = "test4"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

total = 0
nums = []
cards = []

for l in lines:
    words = l.split(':')
    card = int(words[0].split(' ')[-1])
    lists = words[1].split("|")
    mine = list(map(int, filter(str.isdigit, lists[0].strip().split(" "))))
    yours = list(map(int, filter(str.isdigit, lists[1].strip().split(" "))))
    cards.append((card, len(set(mine) & set(yours))))

counts = dict((k[0], 1) for k in cards)
print(counts)

for c in cards:
    factor = counts[c[0]]
    for i in range(c[0] + 1, c[0] + c[1] + 1):
        print(i)
        counts[i] += factor

count = 0
for c in counts:
    count += counts[c]
print(count)


