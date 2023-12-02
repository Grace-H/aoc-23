#!/usr/bin/env python3

filename = "input2"
#filename = "test2"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

total = 0
for l in lines:
    words = l.split(':')
    game = int(words[0].split(' ')[1].strip(':'))
    d = words[1].split(';')
    mm = {"red": [], "green": [], "blue": []}
    for g in d:
        colors = g.split(',')
        for c in colors:
            ms = c.strip().split(' ')
            mm[ms[1].strip()].append(int(ms[0].strip()))

    total += max(mm["red"])*max(mm["green"])*max(mm["blue"]) 
    
print(total)
